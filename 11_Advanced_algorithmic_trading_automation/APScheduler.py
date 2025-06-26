from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
def execute_trading_signal():

# There should be a logic of receiving and processing data, generating a signal and executing a trade
    print(f"Execution of a trade signal in {datetime.datetime.now()}")


# Creating a scheduler
scheduler = BlockingScheduler()
# Run the function every 10 seconds
scheduler.add_job(execute_trading_signal, 'interval', seconds=10)

try:
    print("Starting bot...")
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    print("Bot stopped by user.")