# prometheus-playground
Simple Application that creates 4 docker images, Prometheus, Promethus Push Gateway, and Alert Manager, and a regular client running a cronjob


### Quick start
Create and run docker images: `docker-compose up --build`

Go to graph tab and try and run the following queries:

```
job_failed // instantaneous gauge metric

sum_over_time(job_failed[10m]) // gets numer of failed jobs in the past 10mins
``` 

### Setup

```
python3 -m venv env
pip install -r requirements.txt
```

### TODO

- [ ] Add Graphana
- [ ] Add Alert Manager Support