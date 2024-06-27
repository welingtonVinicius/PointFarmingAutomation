npm install socket.io-client
```

```javascript
import axios from 'axios';
import dotenv from 'dotenv';
import { io } from 'socket.io-client';

dotenv.config();

const backendApiUrl = process.env.BACKEND_URL || 'http://localhost:3000';

const socket = io(backendApiUrl);

const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const siteNameInput = document.getElementById('siteName');
const apiKeyInput = document.getElementById('apiKey');
const progressDisplay = document.getElementById('progressDisplay');

document.getElementById('loginForm').addEventListener('submit', submitLoginForm);
document.getElementById('settingsForm').addEventListener('submit', submitSettingsForm);

async function submitLoginForm(event) {
    event.preventDefault();
    try {
        await axios.post(`${backendApiUrl}/login`, {
            email: emailInput.value,
            password: passwordChat.value,
        });
        alert('Login Successful');
    } catch (error) {
        console.error('Login failed:', error);
        alert('Login Failed');
    }
}

async function submitSettingsForm(event) {
    event.preventDefault();
    try {
        await axios.post(`${backendApiUrl}/settings`, {
            siteName: siteNameInput.value,
            apiKey: apiKeyInput.value,
        });
        alert('Settings Updated');
    } catch (error) {
        console.error('Failed to update settings:', error);
        alert('Failed to Update Settings');
    }
}

async function retrieveFarmingProgress() {
    try {
        const { data: progressData } = await axios.get(`${backendApiUrl}/farmingProgress`);
        progressDisplay.innerHTML = JSON.stringify(progressData, null, 2);
    } catch (error) {
        console.error('Failed to fetch farming progress:', error);
        alert('Failed to Fetch Farming Progress');
    }
}

function setupRealTimeProgressUpdates() {
    socket.on('farmingProgressUpdate', progressUpdate => {
        progressDisplay.innerHTML = JSON.stringify(progressUpdate, null, 2);
    });
}

retrieveFarmingProgress();
setupRealTimeProgressUpdates();