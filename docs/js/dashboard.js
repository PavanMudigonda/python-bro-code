// Dashboard functionality
document.addEventListener('DOMContentLoaded', function() {
    updateDashboard();
    
    // Auto-refresh every 30 seconds
    setInterval(updateDashboard, 30000);
});

function updateDashboard() {
    const progress = progressTracker.getProgress();
    
    // Update overall stats
    document.getElementById('total-completed').textContent = progress.metadata.completed;
    document.getElementById('completion-percentage').textContent = 
        progress.metadata.completion_percentage + '%';
    document.getElementById('current-streak').textContent = progress.streaks.current_streak;
    document.getElementById('achievements-count').textContent = progressTracker.getAchievementCount();
    
    // Update level progress
    updateLevelProgress('beginner', progress.levels.beginner);
    updateLevelProgress('intermediate', progress.levels.intermediate);
    updateLevelProgress('advanced', progress.levels.advanced);
    updateLevelProgress('expert', progress.levels.expert);
    updateLevelProgress('master', progress.levels.master);
    updateLevelProgress('challenge', progress.levels.challenge);
    
    // Update activity
    updateActivity(progress.activity);
}

function updateLevelProgress(level, data) {
    const card = document.querySelector(`.level-card[data-level="${level}"]`);
    if (!card) return;
    
    const progressBar = card.querySelector('.progress-fill');
    const completedSpan = card.querySelector('.completed');
    const percentageSpan = card.querySelector('.percentage');
    
    if (progressBar) {
        progressBar.style.width = data.percentage + '%';
    }
    
    if (completedSpan) {
        completedSpan.textContent = `${data.completed}/${data.total}`;
    }
    
    if (percentageSpan) {
        percentageSpan.textContent = data.percentage + '%';
    }
}

function updateActivity(activities) {
    const activityList = document.getElementById('activity-list');
    if (!activityList) return;
    
    if (activities.length === 0) {
        activityList.innerHTML = '<p class="no-activity">No activity yet. Start solving questions!</p>';
        return;
    }
    
    activityList.innerHTML = activities.slice(0, 10).map(activity => {
        const date = new Date(activity.timestamp);
        const timeAgo = getTimeAgo(date);
        
        return `
            <div class="activity-item">
                <div class="activity-icon">
                    ${activity.type === 'achievement' ? '🏆' : '✅'}
                </div>
                <div class="activity-content">
                    <p><strong>${activity.message}</strong></p>
                    <small>${timeAgo}</small>
                </div>
            </div>
        `;
    }).join('');
}

function getTimeAgo(date) {
    const seconds = Math.floor((new Date() - date) / 1000);
    
    let interval = seconds / 31536000;
    if (interval > 1) return Math.floor(interval) + ' years ago';
    
    interval = seconds / 2592000;
    if (interval > 1) return Math.floor(interval) + ' months ago';
    
    interval = seconds / 86400;
    if (interval > 1) return Math.floor(interval) + ' days ago';
    
    interval = seconds / 3600;
    if (interval > 1) return Math.floor(interval) + ' hours ago';
    
    interval = seconds / 60;
    if (interval > 1) return Math.floor(interval) + ' minutes ago';
    
    return 'Just now';
}

// Add CSS for activity items
const activityStyles = `
.activity-item {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background: #f8f9fa;
    border-radius: 8px;
    transition: background 0.3s;
}

.activity-item:hover {
    background: #e9ecef;
}

.activity-icon {
    font-size: 1.5rem;
}

.activity-content p {
    margin-bottom: 0.25rem;
}

.activity-content small {
    color: var(--gray);
}
`;

// Inject styles
const styleSheet = document.createElement('style');
styleSheet.textContent = activityStyles;
document.head.appendChild(styleSheet);
