# Postmortem
The 500 Internal Server Error Apocalypse
## Issue Summary

   - Duration: February 27, 2025, 13:15 - 14:05 UTC (50 minutes of pure chaos)
    -Impact:
        100% of API requests returned a 500 error, Yes, every. Single. One. (Internal Server Error).
        Web and mobile apps became unusable—users couldn’t log in, retrieve data, or complete transactions.
        Over 5,000 error logs generated per minute.
        Customer support tickets increased by 300% in under an hour.
    -Root Cause:
    A database connection limit was exceeded, causing all requests to fail.

## Timeline

   - 13:15 UTC - Deployment of a backend update. Everything looked fine. Confidence was high. ☀️  
   - 13:17 UTC - Monitoring alerts detected a spike in 500 errors.  
    -13:20 UTC - Reports from users and internal teams confirmed that the system was completely down.  
    -13:25 UTC - Engineers checked server logs—all errors pointed to database connection failures. so we assumed the database server had died. 💀  
    -13:30 UTC - Initial assumption: database server crashed. Investigation showed the database was up but rejecting connections.  
    -13:40 UTC - A deep dive into the latest code changes revealed that a new background job was opening connections but never closing them.  
    -13:45 UTC - Hotfix prepared to properly close connections.  
    -14:00 UTC - Fix deployed, and API requests gradually started succeeding. Users stopped screaming. 🎉  
    -14:05 UTC - System fully operational again.  

## Root Cause and Resolution
- Root Cause:

   - A recent backend update introduced a new background job to process analytics.
   - The job opened a new database connection for every task but never closed them, quickly exhausting the database’s max connection limit.
   - Once the limit was hit, all incoming API requests were rejected, resulting in 500 errors.

- Resolution:

   - Updated the job to close database connections after execution:  
```
    def process_analytics():
        conn = db.connect()
        try:
            run_query(conn)
        finally:
            conn.close()  # Ensuring the connection is properly closed  
```  
   - Deployed the fix, restoring normal operations.  

   - Restarted affected services to clear lingering connections.  

## Corrective and Preventative Measures
### What Can Be Improved?  

    - Better database connection management in background tasks.
    - Increase monitoring on database connection usage. f they spike unexpectedly, sound the alarms.
    - Set up circuit breakers to prevent new jobs from overloading the database.

## TODO List to address the issue:

☑ Implement database connection pooling to manage requests efficiently.
☑ Set up alerts if database connections approach the limit.
☑ Review all background jobs before deployment (no more free-for-all coding).
☑ Simulate heavy traffic in testing to catch issues early.

## Final Thoughts

This incident was a painful reminder that one small oversight in database management can take down an entire system.