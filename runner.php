<?php
include_once 'functions.php';
include_once 'update_performance.php';
include_once 'generate_signals.php';
include_once 'create_options.php';

	
global $conn_signals;
//set time zone:
date_default_timezone_set('Asia/Kolkata');

$from_time  = "2021-11-03 09:15:00";
$to_time	= "2021-11-03 15:30:00";
$time_now   ='';

for ($time_now=$from_time; $time_now <= $to_time; )
{
	$symbols_obj = new Symbol('symbols');
	$symbols_list=$symbols_obj->get_symbols($where='active', $value=1);
	foreach($symbols_list as $symbol_record)
	{
		echo"   ";
		echo $symbol = $symbol_record['symbol'];
		echo"   ";
		$mcandle_obj	= new mcandle($symbol);
		$tablename = $mcandle_obj->tablename;
		//$query = "UPDATE $tablename set active=1";
		echo $query = "UPDATE $tablename set active=0 where stime='$time_now'";
		$response = mysqli_query($conn_signals, $query);
	}
	//exit;
	$time_now = date ("Y-m-d H:i:s", strtotime($time_now."+1 minute"));
	$sub_time = substr($time_now,11,5);
		if($sub_time>'15:30' || isweekend($time_now))
		{
			//this means go to next day
			echo $time_now = substr($time_now,0,10).'09:15:00';
			echo $time_now = date ("Y-m-d H:i:s", strtotime($time_now." +1 day"));
		}
		echo "Time is $time_now <br>";
	echo "Time is $time_now <br>";


	//call function here
	//include_once 'crondata.php';

	cronfunction();
}

function isweekend($date)
{
	return (date('N', strtotime($date)) >= 6);
}

function cronfunction()
{
	$msg		= "Cron Job";
	$dateranges = array();
	$process_candles = $replay_records = array();
	$active='';

	$time=date("h:i:sa");
	echo "Starting $msg at $time <br />";

	$replay_obj = new Replay("replay");
	//$result=$replay_obj->create_table();	

	$symbols_obj = new Symbol('symbols');
	$symbols_list=$symbols_obj->get_symbols($where='active', $value=1);

	foreach($symbols_list as $symbol_record)
	{
		$token			  = $symbol_record['token'];
		$symbol			 = $symbol_record['symbol'];
		$type			   = $symbol_record['type'];
		$expiry			 = $symbol_record['expiry'];
		$update_performance = $symbol_record['update_performance'];
		$generate_candles   = $symbol_record['generate_candles'];
		$merge_candles	  = $symbol_record['merge_candles'];
		$generate_signals   = $symbol_record['generate_signals'];
		$strategy		   = $symbol_record['strategy'];
	
		echo "Current Scock being processed= $symbol <br />";
	 
		$dateranges=get_date_ranges($expiry);
		$data_from	  = $dateranges['data_from'];
		$data_to		= $dateranges['data_to'];
		$signal_from	= $dateranges['signal_from'];
		$signal_to	  = $dateranges['signal_to'];

		
		if (!$dateranges) 
			continue;
			
		$candle_obj	 = new candle($symbol);
		$mcandle_obj	= new mcandle($symbol);

		//  getting candles:

		//we must also see that for options, we need not get data from the beginning of time, or data_from. We only need to get from today to today day end
	   if ($data_from!='' and $data_to!='' and $generate_candles)
		{
			if($type=='OPTION')
			{
				$data_from_option = date("Y-m-d");
				//get_candles($symbol,$token,$data_from_option,$data_to,$candle_obj);
			}
			
			else
			{
				//get_candles($symbol,$token,$data_from,$data_to,$candle_obj);
			}
			
		}

		//  inserting candles into merge tables:
		
		if ($merge_candles) 
		{
			//merge_candles($symbol,$data_from,$data_to,$candle_obj,$mcandle_obj);
		}
		
		// get merged candles
	
		$process_candles = get_merged_candles($symbol,$signal_from,$signal_to,$active='0',$mcandle_obj);
		if ($process_candles)
		{
			foreach($process_candles as $process_candle)
			{
				//mopving each record into the replay table and then setting that merged record as active=1
				$replay_obj->put_record($process_candle);
				//updating to set active
				$mcandle_obj->update_status($symbol,$process_candle['id'], $active=1);
			}
		}
		// Get record to be processed 
		
		$replay_records=get_replay_records($replay_obj);
		
		if(sizeof($replay_records)==0)
			continue;
		//process merged records:
		
		if ($replay_records)
			process_merged_candles($replay_records,$symbols_obj,$replay_obj,$mcandle_obj);
	}

	$msg				= "Cron Job";
	$curr_time=date('Y-m-d H:i:s');
	echo "End $msg at $time <br />";
}

function get_candles($symbol, $token, $data_from,$data_to, $candle_obj)
{
	$success=0;
	
	$curr_date=date('Y-m-d');
	$curr_time=date('Y-m-d H:i:s');
	$msg		= 'Getting Candle Data';
	
	echo "Start...$msg from $data_from to $data_to @$curr_time <br />";

	if (!$candle_obj->check_table())
		$candle_obj->create_table();
		
		$candle_obj->get_historicaldata($token, $symbol,  $frequency=1,  $data_from, $data_to);  
		$candle_obj->get_historicaldata($token, $symbol,  $frequency=3,  $data_from, $data_to);  
		$candle_obj->get_historicaldata($token, $symbol,  $frequency=5,  $data_from, $data_to);  
		$candle_obj->get_historicaldata($token, $symbol,  $frequency=15, $data_from, $data_to);  
		$candle_obj->get_historicaldata($token, $symbol,  $frequency=30, $data_from, $data_to);  
		$candle_obj->get_historicaldata($token, $symbol,  $frequency=60, $data_from, $data_to);  
	
		$success=1;

	$curr_time=date('Y-m-d H:i:s');
	echo "End...$msg @$curr_time <br />";
	
	return ($success);
}

function merge_candles($symbol,$data_from,$data_to,$candle_obj,$mcandle_obj)
{
	$msg		= 'Merging Candles into another table';
	$curr_time=date('Y-m-d H:i:s');

	$candles_list= array ();
	$last_mcandle_time='';
  
	echo "Start...$msg from $data_from to $data_to @$curr_time <br />";

	// Check if the respective candle table exists

	if (!$mcandle_obj->check_table())
		$mcandle_obj->create_table();
  
	// Get the last merged mcandle //
	$mcandle=$mcandle_obj->get_last_record($symbol);

	if (!isset($mcandle['stime'])) 
		$last_mcandle_time='';
	else
		$last_mcandle_time=$mcandle['stime'];

	if ($last_mcandle_time != '')
		$data_from=$last_mcandle_time;

	$candles_list=$candle_obj->get_candles($symbol, $frequency=1, $data_from, $data_to, $active='0');
	//print_r($candles_list);
	
	foreach($candles_list as $candle)
	{
		$mcandle = array();
	   
		$id=$candle['id'];
		$stime=$candle['stime'];

		$mcandle=$candle_obj->get_merged_candle($symbol, $stime);
		//print_r($mcandle);

		//check if merged candle exists //
		$existing_candle=$mcandle_obj->get_candle($symbol, $stime);
		//print_r($existing_candle);
		if (!isset($existing_candle['stime']))
		{
			$mcandle_obj->put_candle($mcandle);
			$candle_obj->update_status($symbol, $id, $active=1);
		}
	
	}

	$curr_time=date('Y-m-d H:i:s');
	echo "End...$msg @$curr_time <br />";	
}

function get_merged_candles($symbol, $signal_from,$signal_to,$active,$mcandle_obj)
{
	$process_candles = array();

	$curr_time=date('Y-m-d H:i:s');
	$msg = "Getting Merged Candles";
	echo "Start...$msg from $signal_from to $signal_to @$curr_time <br />";

	
	$process_candles=$mcandle_obj->get_candles($symbol,$from_time=$signal_from, $to_time=$signal_to,$active);

	$curr_time=date('Y-m-d H:i:s');
	echo "End...$msg from $signal_from to $signal_to  @$curr_time <br />";
	
   return ($process_candles);
}

function get_replay_records($replay_obj)
{
	$replay_records = array ();
	$replay_records=$replay_obj->get_records($from_time='',$to_time='',$active='0');
	return ($replay_records['data']);
}

function process_merged_candles($process_candles,$symbols_obj,$replay_obj,$mcandle_obj)
{
	$success=0;
	
	$strategy_obj   = new strategy("strategy");
	$parameters_obj = new parameters("parameters");
	$signal_obj	 = new signal("signals");
	
	$current_candle=$prev_candle=array();	
	
	foreach($process_candles as $process_candle)
	{
		$replay_id = $process_candle['replay_id'];
		$current_candle=$process_candle['data'];
		
		
		$prev_candle = $replay_obj->get_prev_record($current_candle['symbol'],$current_candle['stime']);
		
		$symbol=$current_candle['symbol'];
		$symbol_record=$symbols_obj->get_symbol($where='symbol', $value=$symbol);
		
		$token			  = $symbol_record['token'];
		$type			   = $symbol_record['type'];
		$expiry			 = $symbol_record['expiry'];
		$generate_candles   = $symbol_record['generate_candles'];
		$merge_candles	  = $symbol_record['merge_candles'];
		$update_performance = $symbol_record['update_performance'];
		$generate_signals   = $symbol_record['generate_signals'];
		$strategy		   = $symbol_record['strategy'];
		$active			 = $symbol_record['active'];
		
		$app_parameters=$parameters_obj->get_parameters('autotrades');
		$quantity=calc_quantity($symbol_record['type'], $symbol_record['price'], $symbol_record['trade_amt'], $symbol_record['margin_pcnt'], $symbol_record['lotsize']);
		
		$strategy_parameters = $strategy_obj->get_strategy($symbol_record['strategy']);
		
		$trade_parameters['trade_start_time']=$app_parameters['trade_start_time'];
		$trade_parameters['trade_end_time']=$app_parameters['trade_end_time'];
		$trade_parameters['quantity']=$quantity;
		$trade_parameters['type']=$symbol_record['type'];
  
		if ($update_performance) 
			update_performance_helper($signal_obj, $current_candle, $strategy_parameters);
		if($type=='FUTURE')
		{
		    options_root($symbol_record,$current_candle['stime']);
		}
		
		if ($generate_signals)
			{
				$generate_result=generate_signals_check($signal_obj, $current_candle, $prev_candle, $strategy_parameters, $trade_parameters);
				
			  	if (isset($generate_result['success']) and $generate_result['success'])
				{
					$symbol		 = $generate_result['symbol'];
					$symbol_type	= $generate_result['symbol_type'];
					$trade		  = $generate_result['trade'];
					$price		  = $generate_result['price'];
					$stime		  = $generate_result['stime'];
					$sl			 = $generate_result['sl'];
					
					/*if ($app_parameters['regular_options'])
					{
						#create_options_check($option='REGULAR', $symbol, $symbol_type, $trade, $price, $stime, $signal_obj);
					}
					else{}
					if ($app_parameters['hedged_options'])
					{
						#create_options_check($option='HEDGED', $symbol, $symbol_type, $trade, $sl, $stime, $signal_obj);
					}
					else{}*/
					if($trade=='EXIT' and $symbol_type!='OPTION')
					{
						//we are checking if we need to generate new signal here
						/*echo"*******";
						echo"<br>";
						print_r($current_candle);
						echo"<br>";
						print_r($prev_candle);
						echo"<br>";
						echo"*******";*/
						
						$generate_result=generate_signals_check($signal_obj, $current_candle, $prev_candle, $strategy_parameters, $trade_parameters);
						
						if (isset($generate_result['success']) and $generate_result['success'])
						{
							$symbol		 = $generate_result['symbol'];
							$symbol_type	= $generate_result['symbol_type'];
							$trade		  = $generate_result['trade'];
							$price		  = $generate_result['price'];
							$stime		  = $generate_result['stime'];
							$sl			 = $generate_result['sl'];
					
					
							/*if ($app_parameters['regular_options'])
							{
								#create_options_check($option='REGULAR', $symbol, $symbol_type, $trade, $price, $stime, $signal_obj);
							}
							if ($app_parameters['hedged_options'])
							{
								#create_options_check($option='HEDGED', $symbol, $symbol_type, $trade, $sl, $stime, $signal_obj);
							}*/
						}
					}
					else{}
					if($trade=='EXIT' and $symbol_type=='OPTION')
                    {
                        //we need to remove option here
                        remove_option_instrument($symbol);
                        $replay_obj->remove_replay_record($current_candle);
                    }
				}
			}
		
		
		//after the record is processed, we set active = 1 for that record
		
		$replay_obj->update_status($replay_id,$active=1);
	}
	
	return($success);
}


?>