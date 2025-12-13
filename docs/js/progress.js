// Progress tracking in localStorage
const STORAGE_KEY = 'python-practice-progress';

class ProgressTracker {
    constructor() {
        this.loadProgress();
    }

    loadProgress() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
            this.data = JSON.parse(stored);
        } else {
            this.data = this.getDefaultProgress();
        }
    }

    getDefaultProgress() {
        return {
            metadata: {
                total_questions: 1000,
                completed: 0,
                in_progress: 0,
                not_started: 1000,
                last_updated: null,
                start_date: null,
                completion_percentage: 0.0
            },
            levels: {
                beginner: { total: 100, completed: 0, percentage: 0.0, questions: {} },
                intermediate: { total: 200, completed: 0, percentage: 0.0, questions: {} },
                advanced: { total: 200, completed: 0, percentage: 0.0, questions: {} },
                expert: { total: 200, completed: 0, percentage: 0.0, questions: {} },
                master: { total: 200, completed: 0, percentage: 0.0, questions: {} },
                challenge: { total: 100, completed: 0, percentage: 0.0, questions: {} }
            },
            achievements: {
                python_apprentice: false,
                python_practitioner: false,
                python_expert: false,
                bronze_medal: false,
                silver_medal: false,
                gold_medal: false,
                diamond_tier: false,
                grand_master: false,
                speed_demon: false,
                space_optimizer: false,
                innovator: false,
                category_master: [],
                on_fire: false,
                ultimate_champion: false
            },
            streaks: {
                current_streak: 0,
                longest_streak: 0,
                last_activity: null
            },
            activity: []
        };
    }

    saveProgress() {
        this.data.metadata.last_updated = new Date().toISOString();
        localStorage.setItem(STORAGE_KEY, JSON.stringify(this.data));
    }

    markQuestionComplete(questionNumber, level, timeTaken = null) {
        const levelData = this.data.levels[level];
        if (!levelData) return;

        // Mark question as complete
        if (!levelData.questions[questionNumber]) {
            levelData.questions[questionNumber] = {
                completed: true,
                completed_at: new Date().toISOString(),
                time_taken: timeTaken,
                attempts: 1
            };
            
            levelData.completed++;
            levelData.percentage = (levelData.completed / levelData.total * 100).toFixed(1);
            
            // Update metadata
            this.data.metadata.completed++;
            this.data.metadata.not_started--;
            this.data.metadata.completion_percentage = 
                (this.data.metadata.completed / this.data.metadata.total_questions * 100).toFixed(1);
            
            // Update streak
            this.updateStreak();
            
            // Check achievements
            this.checkAchievements();
            
            // Add to activity
            this.addActivity(`Completed Question ${questionNumber}`, level);
            
            // Save
            this.saveProgress();
            
            return true;
        }
        return false;
    }

    updateStreak() {
        const now = new Date();
        const lastActivity = this.data.streaks.last_activity 
            ? new Date(this.data.streaks.last_activity) 
            : null;
        
        if (!lastActivity) {
            this.data.streaks.current_streak = 1;
            this.data.streaks.longest_streak = 1;
        } else {
            const daysDiff = Math.floor((now - lastActivity) / (1000 * 60 * 60 * 24));
            
            if (daysDiff === 0) {
                // Same day, keep streak
            } else if (daysDiff === 1) {
                // Next day, increment streak
                this.data.streaks.current_streak++;
                if (this.data.streaks.current_streak > this.data.streaks.longest_streak) {
                    this.data.streaks.longest_streak = this.data.streaks.current_streak;
                }
            } else {
                // Streak broken
                this.data.streaks.current_streak = 1;
            }
        }
        
        this.data.streaks.last_activity = now.toISOString();
    }

    checkAchievements() {
        const completed = this.data.metadata.completed;
        const achievements = this.data.achievements;
        
        if (completed >= 50 && !achievements.python_apprentice) {
            achievements.python_apprentice = true;
            this.addActivity('🎉 Achievement Unlocked: Python Apprentice!', 'achievement');
        }
        if (completed >= 100 && !achievements.python_practitioner) {
            achievements.python_practitioner = true;
            this.addActivity('🎉 Achievement Unlocked: Python Practitioner!', 'achievement');
        }
        if (completed >= 200 && !achievements.python_expert) {
            achievements.python_expert = true;
            this.addActivity('🎉 Achievement Unlocked: Python Expert!', 'achievement');
        }
        if (completed >= 300 && !achievements.bronze_medal) {
            achievements.bronze_medal = true;
            this.addActivity('🥉 Achievement Unlocked: Bronze Medal!', 'achievement');
        }
        if (completed >= 500 && !achievements.silver_medal) {
            achievements.silver_medal = true;
            this.addActivity('🥈 Achievement Unlocked: Silver Medal!', 'achievement');
        }
        if (completed >= 700 && !achievements.gold_medal) {
            achievements.gold_medal = true;
            this.addActivity('🥇 Achievement Unlocked: Gold Medal!', 'achievement');
        }
        if (completed >= 900 && !achievements.diamond_tier) {
            achievements.diamond_tier = true;
            this.addActivity('💎 Achievement Unlocked: Diamond Tier!', 'achievement');
        }
        if (completed >= 1000 && !achievements.grand_master) {
            achievements.grand_master = true;
            this.addActivity('🏆 Achievement Unlocked: GRAND MASTER!', 'achievement');
        }
    }

    addActivity(message, type = 'question') {
        this.data.activity.unshift({
            message,
            type,
            timestamp: new Date().toISOString()
        });
        
        // Keep only last 50 activities
        if (this.data.activity.length > 50) {
            this.data.activity = this.data.activity.slice(0, 50);
        }
    }

    getProgress() {
        return this.data;
    }

    getLevelProgress(level) {
        return this.data.levels[level];
    }

    getAchievementCount() {
        return Object.values(this.data.achievements).filter(a => a === true).length;
    }

    exportProgress() {
        return JSON.stringify(this.data, null, 2);
    }

    importProgress(jsonData) {
        try {
            this.data = JSON.parse(jsonData);
            this.saveProgress();
            return true;
        } catch (e) {
            console.error('Failed to import progress:', e);
            return false;
        }
    }

    resetProgress() {
        if (confirm('Are you sure you want to reset all progress? This cannot be undone!')) {
            this.data = this.getDefaultProgress();
            this.saveProgress();
            return true;
        }
        return false;
    }
}

// Global instance
const progressTracker = new ProgressTracker();
