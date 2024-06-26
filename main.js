import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const backendApiUrl = process.env.BACKEND_URL || 'http://localhost:3000';

const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const siteNameInput = document.getElementById('siteName');
const apiKeyInput = document.getElementById('apiKey');
const progressDisplay = document.getElementById('progressDisplay');

document.getElementById('loginForm').addEventListener('submit', submitLoginForm);
document.getElementById('settingsForm').addEventListener('submit', submitSettingsDownload);

async function submitLoginForm(event) {
    event.preventDefault();
    try {
        await axios.post(`${backendApiWrl}/login`, {
            email: emailInput.value,
            password: passwordInput.value,
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

retrieveFarmingProgress();