from playwright.sync_api import Playwright

def pytest_playwright_browser_context_args():
    return {
        "record_video_dir": "videos/",
        "record_har_path": "network_logs.har",
        "ignore_https_errors": True
    }