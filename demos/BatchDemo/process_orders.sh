#!/bin/bash
while true; do
    echo -e '\nProcessing Orders...'
    # Show what we're about to 'process'
    head -n 5 pending_orders.txt
    # Delete from the pending_orders file.
    sed -i '1,5d' pending_orders.txt
    # Print remaining orders.
    echo -e 'Orders Remaining: ' $(wc -l < pending_orders.txt)
    # Wait (seconds)
    sleep 5
done
