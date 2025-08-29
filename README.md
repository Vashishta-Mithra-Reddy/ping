# Service Ping Monitor

A lightweight Python utility that monitors web service availability by sending periodic HTTP requests. This tool is designed to keep services active and monitor their health status, particularly useful for preventing free-tier hosting services from going to sleep.

## 🚀 Features

- **Automated Service Monitoring**: Ping multiple endpoints to check availability
- **GitHub Actions Integration**: Runs automatically every 10 minutes
- **Error Handling**: Robust error handling with detailed logging
- **Configurable Timeouts**: Customizable request timeout settings  
- **Easy Configuration**: Simple endpoint management
- **Manual Execution**: Can be run locally or triggered manually

## 📋 Requirements

- Python 3.9 or higher
- Internet connection for endpoint monitoring

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vashishta-Mithra-Reddy/ping.git
   cd ping
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Usage

### Local Execution

Run the ping script manually:

```bash
python ping_script.py
```

This will:
- Send HTTP GET requests to all configured endpoints
- Log the response status codes for successful requests
- Log error messages for failed requests
- Complete execution and exit

### Automated Execution

The repository includes GitHub Actions workflow that:
- Runs automatically every 10 minutes (`*/10 * * * *` cron schedule)
- Can be manually triggered from the Actions tab
- Installs dependencies and executes the ping script
- Logs results in the GitHub Actions console

## ⚙️ Configuration

### Adding/Modifying Endpoints

Edit the `endpoints` list in `ping_script.py`:

```python
def ping_endpoints():
    endpoints = [
        "https://your-service-1.onrender.com/",
        "https://your-service-2.herokuapp.com/",
        "https://example.com/health",
        # Add more endpoints as needed
    ]
```

### Adjusting Request Timeout

Modify the timeout parameter in the requests call:

```python
response = requests.get(url, timeout=10)  # 10 seconds timeout
```

### Customizing Log Level

Change the logging level in the `main()` function:

```python
logging.basicConfig(level=logging.INFO)  # Options: DEBUG, INFO, WARNING, ERROR
```

## 🏗️ Project Structure

```
ping/
├── .github/
│   └── workflows/
│       └── main.yml          # GitHub Actions workflow
├── ping_script.py            # Main ping functionality
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🤖 GitHub Actions Workflow

The automated workflow (`main.yml`) includes:

- **Schedule**: Runs every 10 minutes
- **Manual Trigger**: Can be run on-demand via workflow_dispatch
- **Environment**: Ubuntu latest with Python 3.9
- **Steps**:
  1. Checkout repository
  2. Set up Python environment
  3. Install dependencies
  4. Execute ping script

### Manual Workflow Trigger

1. Go to the "Actions" tab in your GitHub repository
2. Select "Ping Services" workflow
3. Click "Run workflow" 
4. Choose branch and click "Run workflow"

## 📊 Monitoring and Logs

### Local Logs
When running locally, logs are output to the console:
```
INFO:root:Pinged https://example.com/. Status code: 200
ERROR:root:Error pinging https://down-service.com/: Connection timeout
```

### GitHub Actions Logs
View execution logs in:
1. Repository → Actions tab
2. Select workflow run
3. Click on "ping-services" job
4. Expand "Run Ping Script" step

## 🐛 Troubleshooting

### Common Issues

**Connection Timeouts:**
- Check if the target service is running
- Verify the URL is correct and accessible
- Consider increasing the timeout value

**DNS Resolution Errors:**
- Ensure the domain name is valid
- Check if the service is temporarily down
- Verify internet connectivity

**Import Errors:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version compatibility

### Debug Mode

Enable debug logging for more detailed output:

```python
logging.basicConfig(level=logging.DEBUG)
```

## 💡 Use Cases

- **Free Tier Services**: Keep Render, Heroku, or other free hosting services active
- **Health Monitoring**: Regular health checks for web applications
- **Service Discovery**: Test service availability in CI/CD pipelines
- **Uptime Monitoring**: Basic monitoring solution for small projects

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Test your changes locally
5. Commit your changes (`git commit -am 'Add new feature'`)
6. Push to the branch (`git push origin feature/improvement`)
7. Create a Pull Request

### Development Setup

```bash
# Install development dependencies (if any)
pip install -r requirements.txt

# Run tests (if available)
python -m pytest

# Run the script locally for testing
python ping_script.py
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Related Projects

- [requests](https://docs.python-requests.org/) - HTTP library for Python
- [schedule](https://schedule.readthedocs.io/) - Job scheduling library

---

**Note**: This tool is designed for legitimate service monitoring purposes. Please ensure you have permission to ping the endpoints you configure and respect rate limiting policies of target services. 
