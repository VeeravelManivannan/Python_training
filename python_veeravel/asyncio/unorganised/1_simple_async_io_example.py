#simple python example to illustrate async io functionality

import asyncio

async def coroutine_which_sleeps_for_10_seconds():
	print("coroutine_which_sleeps_for_10_seconds has started to sleep")
	await asyncio.sleep(10)
	print("the attention of the scheduler is now back to coroutine_which_sleeps_for_10_seconds ")
	
async def coroutine_which_sleeps_for_5_seconds():
	print("coroutine_which_sleeps_for_5_seconds has started to sleep")
	await asyncio.sleep(5)
	print("the attention of the scheduler is now back to coroutine_which_sleeps_for_5_seconds ")
	
	
async def worker_coroutine():
		#Task list , which contains all the co-routing objects 
		taskslist = [coroutine_which_sleeps_for_10_seconds(),coroutine_which_sleeps_for_5_seconds()]
		#It is always , good to write await inside "co-routines" , since it is always good to keep the code completely asynchronous 
		await asyncio.gather(*taskslist)
		#asyncio.gather(*taskslist)
		
		
#main code starts here , when we use the run() function , we need not create the event loop (It takes care of the event loop creation by itself )
asyncio.run(worker_coroutine())		
	
	
	
	