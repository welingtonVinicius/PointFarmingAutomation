import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const backendURL = process.env.BACKEND_URL || 'http://localhost:3000';

document.getElementById('loginForm').addEventListener('submit', handleLogin);
document.getElementById('settingsForm').addEventListener('submit', handleSettings);

async function handleLogin(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await axios.post(`${backendURL}/login`, { email, password });
        alert('Login Successful');
    } catch (error) {
        console.error('Login failed:', error);
        alert('Login Failed');
    }
}

async function handleSettings(event) {
    event.preventDefault();
    const siteCredentials = {
        siteName: document.getElementById('siteName').value,
        apiKey: document.getElementById('apiKey').value,
    };

    try {
        const response = await axios.post(`${backendURL}/settings`, siteCredentials);
        alert('Settings Updated');
    } catch (error) {
        console.error('Failed to update settings:', error);
        alert('Failed to Update Settings');
    }
}

async function fetchFarmingProgress() {
    try {
        const response = await axios.get(`${backendURL}/farmingProgress`);
        const progressData = response.data;
        document.getElementById('progressDisplay').innerHTML = JSON.stringify(progressData, null, 2);
    } catch (error) {
        console.error('Failed to fetch farming progress:', error);
        alert('Failed to Fetch Farming Progress');
    }
}

fetchFarmingProgress();