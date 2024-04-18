import queue
import time

## #####################################################################
## EVENT HANDLERS
## #####################################################################
def handle_greeting():
    print("Hello!")

def handle_goodbye():
    print("Goodbye!")

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
            event_queue.put(event)
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

        # Get the function to handle the event
        handler = event_handlers.get(event)

        # Call the function to handle the event
        handler()

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
        'goodbye': handle_goodbye,
    }

    # Queue the events. We are simulating events that would
    # normall happen from interacting with the program in real time.
    queue_user_events(event_queue, event_handlers)

    # Process the events in the queue
    event_loop(event_queue, event_handlers)

main()
