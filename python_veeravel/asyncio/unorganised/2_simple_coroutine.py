import asyncio

@asyncio.coroutine
def countdown_in_Seconds(name , no_of_times_count_down):
#async def countdown_in_Seconds(name , no_of_times_count_down):
	while no_of_times_count_down > 0 :
		print("sleeping for 1 seconds for task %s , %d" % name  % no_of_times_count_down)
		yield from asyncio.sleep(1)
		print("sleeping finished %s , %d" % name  % no_of_times_count_down)
		no_of_times_count_down = no_of_times_count_down - 1 
		
		
loop = asyncio.get_event_loop()	
tasklist = [asyncio.ensure_future(countdown("taskA", 5)),asyncio.ensure_future(countdown("taskb", 7))]
loop.run_until_complete(asyncio.wait(tasklist))
loop.close()
		
	
	
