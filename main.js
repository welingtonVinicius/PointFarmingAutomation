import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const backendApiUrl = process.env.BACKEND_URL || 'http://localhost:3000';

document.getElementById('loginForm').addEventListener('submit', submitLoginForm);
document.getElementById('settingsForm').addEventListener('submit', submitSettingsForm);

async function submitLoginForm(event) {
    event.preventDefault();
    const userEmail = document.getElementById('email').value;
    const userPassword = document.getElementById('password').value;

    try {
        const { data: loginResponse } = await axios.post(`${backendApiUrl}/login`, { email: userEmail, password: userPassword });
        alert('Login Successful');
    } catch (error) {
        console.error('Login failed:', error);
        alert('Login Failed');
    }
}

async function submitSettingsForm(event) {
    event.preventDefault();
    const siteConfiguration = {
        siteName: document.getElementById('siteName').value,
        apiKey: document.getElementById('apiKey').value,
    };

    try {
        const { data: settingsResponse } = await axios.post(`${backendApiUrl}/settings`, siteConfiguration);
        alert('Settings Updated');
    } catch (error) {
        console.error('Failed to update settings:', error);
        alert('Failed to Update Settings');
    }
}

async function retrieveFarmingProgress() {
    try {
        const { data: progressData } = await axios.get(`${backendApiUrl}/farmingProgress`);
        document.getElementById('progressDisplay').innerHTML = JSON.stringify(progressData, null, 2);
    } catch (error) {
        console.error('Failed to fetch farming progress:', error);
        alert('Failed to Fetch Farming Progress');
    }
}

retrieveFarmingProgress();