import asyncio
import time

#running a single coroutine directly 
'''
async def countdown(taskname , counter):
	while counter > 0:
		print("task  started at time value of counter is  %s" %taskname)
		print(f"started at {time.strftime('%X')}")
		await asyncio.sleep(2)
		print("Slept for 2 seconds ")
		print(f"finished at  {time.strftime('%X')}")
		print("****************************************")
		counter = counter -1 
		
		
		
#running a simple co-routine
asyncio.run(countdown("task A" , 5))
'''		
	
#running two co routines using a parent co routine  , inference -> only tasks will be scheduled concurrently (is co routine wrapped in a task) and not whne a parent co-routine calls two child co-routine 
#
'''
async def countdown(taskname , counter):
	while counter > 0:
		print("task  started at time value of counter is  %s" %taskname)
		print(f"started at {time.strftime('%X')}")
		await asyncio.sleep(1)
		print("Slept for 2 seconds ")
		print(f"finished at  {time.strftime('%X')}")
		print("****************************************")
		counter = counter -1 
		
#another main co-routine , which will call two co-routines 	, which will inturn await on those two called co-routines 	
		
async def main():
	print("Main started")
	print(f"started at {time.strftime('%X')}")
	print("+++++++++++++++++++++++++++++++++")
	await countdown("taska" , 4)
	await countdown("taskb" , 3)
	await countdown("taskc" , 3)
	print("Main Finished")
	print(f"started at {time.strftime('%X')}")
	print("+++++++++++++++++++++++++++++++++")
		
		
#running a simple co-routine
asyncio.run(main())
#
'''	


#running two co routines using a parent co routine , but this time using the task approach -> inference only tasks will be scheduled concurrently (is co routine wrapped in a task)
#
'''
async def countdown(taskname , counter):
	while counter > 0:
		print("task  started at time value of counter is  %s" %taskname)
		print(f"started at {time.strftime('%X')}")
		await asyncio.sleep(1)
		print("Slept for 2 seconds ")
		print(f"finished at  {time.strftime('%X')}")
		print("****************************************")
		counter = counter -1 
		
#another main co-routine , which will call two co-routines 	, which will inturn await on those two called co-routines 	
		
async def main():
	print("Main started")
	print(f"started at {time.strftime('%X')}")
	print("+++++++++++++++++++++++++++++++++")
	task1 = asyncio.create_task(countdown("taska" , 4))
	task2 = asyncio.create_task(countdown("taskb" , 3))
	task3 = asyncio.create_task(countdown("taskc" , 3))
	await task1
	await task2
	await task3
	print("Main Finished")
	print(f"started at {time.strftime('%X')}")
	print("+++++++++++++++++++++++++++++++++")
		
		
#running a simple co-routine
asyncio.run(main())
#
'''	

# taking a deeper dive at tasks(similar to previois example , what will happend when there i sno await on tasks)

async def some_couroutine_which_sleeps_and_prints(message , no_of_times):
	while no_of_times > 0:
		print(message)
		await asyncio.sleep(1)
		#time.sleep(1)
		no_of_times = no_of_times - 1 
		print("returning from iteration: %d for task: %s" %(no_of_times , message))
		
async def main():
	print(f"started at {time.strftime('%X')}")		
	#task1 = asyncio.create_task(some_couroutine_which_sleeps_and_prints("advancing in python slowly",10))
	#task2 = asyncio.create_task(some_couroutine_which_sleeps_and_prints("advancing in python slowly-task2",10))
	
	#Create_task is probably the same as ensure future
	task1 = asyncio.ensure_future(some_couroutine_which_sleeps_and_prints("advancing in python slowly",10))
	task2 = asyncio.ensure_future(some_couroutine_which_sleeps_and_prints("advancing in python slowly-task2",10))
	task3 = asyncio.ensure_future(some_couroutine_which_sleeps_and_prints("advancing in python slowly-task3",10))
	await task1 
	await task2	
	await task3	
	print(f"ended at {time.strftime('%X')}")
	
asyncio.run(main())	
	
	
#to:do: Running Tasks Concurrently (awaitable asyncio.gather)	
	
	
