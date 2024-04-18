import queue
import time

## #####################################################################
## EVENT HANDLERS
## #####################################################################
def handle_greeting( name ):
    print(f"Hello {name}!")

def handle_add_one( number ):
    # To keep this example simple, we will assume the user
    # enters a valid number.
    number = float(number)
    print(f"{number} + 1 = {number + 1}")

## #####################################################################
## USER INPUT
## #####################################################################
def queue_user_events(event_queue, event_handlers):
    # Simulating adding events to the queue
    while True:
        event = input("Enter an event (q when finished): ")

        # Exit the loop if the user enters 'q'
        if event == 'q':
            break

        # Queue the event if it is in the event_handlers dictionary
        if event in event_handlers:
            argument = input("Enter an argument: ")
            event_queue.put((event, argument))
        else:
            print("Unknown event")

## #####################################################################
## EVENT LOOP
## #####################################################################
def event_loop(event_queue, event_handlers):
    # As long as the queue is not empty, process the events
    while not event_queue.empty():
        # Get the next event from the queue
        event = event_queue.get()

        # Get the event name and arguments
        event_name = event[0]

        # There may be multiple arguments, so we slice the list
        event_args = event[1:]

        # Get the function to handle the event
        handler = event_handlers.get(event_name)

        # Call the function to handle the event
        # The * unpacks the list of arguments
        handler(*event_args)

        # Slow down the loop for demonstration purposes
        time.sleep(.5)

    # Exit the program
    print('No more events to process. Exiting...')

def main():
    # Create a queue to hold events
    event_queue = queue.Queue()

    # Mapping of events to functions
    # Normal programs have events such as button clicks, key presses, etc.
    event_handlers = {
        'greet': handle_greeting,
        'add_one': handle_add_one,
    }

    # Queue the events. We are simulating events that would
    # normall happen from interacting with the program in real time.
    queue_user_events(event_queue, event_handlers)

    # Process the events in the queue
    event_loop(event_queue, event_handlers)

main()
