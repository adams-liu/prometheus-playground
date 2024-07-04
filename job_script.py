import random
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Configure your Push Gateway address here
PUSHGATEWAY_ADDRESS = 'pushgateway:9091'

def process_data():
    """Simulate data processing with random success or failure."""
    # Simulate a process that can succeed or fail
    return random.choice([True, False])

def main():

    # Create a registry to hold the metrics
    registry = CollectorRegistry()
    
    # Define a gauge metric to count the number of job executions
    job_executions = Gauge('job_executions', 'Number of times the job has run', registry=registry)
    job_success = Gauge('job_success', 'Number of successful executions', registry=registry)
    job_failed = Gauge('job_failed', 'Number of failed executions', registry=registry)
    
    # Process some data and record success
    for i in range(10):
        job_executions.inc()
        if process_data():
            job_success.inc()
        else:
            job_failed.inc()
    print("Success: Executed 10 Times!")
    
    # Push the metrics to the Prometheus Push Gateway
    push_to_gateway(PUSHGATEWAY_ADDRESS, job='example_python_job', registry=registry)

if __name__ == "__main__":
    main()