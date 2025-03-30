from temporalio.worker import Worker
from temporalio.client import Client
import asyncio
from workflows import MyWorkflow

async def main():
    # Connect to Temporal Server (running on EC2)
    client = await Client.connect("34.228.166.199:7233")

    # Start the worker
    worker = Worker(
        client,
        task_queue="my-task-queue",
        workflows=[MyWorkflow]
    )
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
