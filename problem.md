### Question
Design a system that will be used to fetch google analytics metrics (e.g. # of visitors, # of unique visitors, # of ppl performing an action,.. ) to monitor website performances for multiple users.
- System should be able to handle up to 100 users
- Each user can add multiple google analytics account to the system, up to 50 accounts
- For each account, user can select up to 200 metrics to fetch everyday,
- Example:
  - User A signs up and connect account A1, A2
  - For account A1 he wants metrics: impressions
  - For account A2 he wants metrics: unique visitors, and number of clicks on buttonA
  - User B signs up and connect account B1
  - For account B1 he wants metrics: unique visitor by country
- We will only focus on synchronous metrics APIs: an API call that returns the metrics right
away
- Calling GET `https://ga.com/metric?accountID=<accountID>&apiKey=<apiKey>&metricName=visitors` returns {result:5}
- There is a per account rate limit on how frequent we can fetch the metrics: The system
should not call google API for a particular account (e.g. account A1 for user A) more than
100 times in 1 hour.
- There is also a global limit: All accounts combined, we cannot call google more than
50000 times in 1 hour.
- There is a 0.001% error rate for API calls, if it fails we need to retry the API, up to 3
times.
- The fetch job will get triggered by a cron job at midnight, and the system should try to
complete all fetches as fast as possible.
The design should be in either a google doc or a PDF file, the length should not be more than 5
pages.

### Notes & Assumptions:
- The system already has a user datastore which can return the list of all users, their
google analytics credentials, and the list of metrics they want to fetch.
- The system also has a metric value datastore, where you can store the metric
ID/account ID /user ID/metric value for a particular day.
- The system should be deployable on AWS cloud.