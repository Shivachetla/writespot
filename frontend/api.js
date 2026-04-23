const API_URL = '/api';

const api = {
    async getStories(category = '') {
        const url = category ? `${API_URL}/stories?category=${category}` : `${API_URL}/stories`;
        const response = await fetch(url);
        return await response.json();
    },

    async login(username, password) {
        const response = await fetch(`${API_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });
        const data = await response.json();
        if (response.ok) {
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('user', JSON.stringify(data.user));
        }
        return data;
    },

    async signup(username, email, password) {
        const response = await fetch(`${API_URL}/auth/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, email, password })
        });
        return await response.json();
    },

    async createStory(storyData) {
        const token = localStorage.getItem('token');
        const response = await fetch(`${API_URL}/stories`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(storyData)
        });
        return await response.json();
    },

    async getBooks() {
        const response = await fetch(`${API_URL}/books`);
        return await response.json();
    },

    logout() {
        localStorage.removeItem('token');
        localStorage.removeItem('user');
    },

    isAuthenticated() {
        return !!localStorage.getItem('token');
    },

    getCurrentUser() {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    }
};
