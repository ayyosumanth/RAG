// MSME Market Intelligence RAG Chatbot Application
class MSMEIntelligenceApp {
    constructor() {
        this.companies = [
            {
                "Company_ID": "MSME001",
                "Company_Name": "Oilmax Systems Pvt Ltd", 
                "Sector": "Manufacturing",
                "Location": "Chennai, Tamil Nadu",
                "Founded_Year": 1995,
                "Employee_Count": 199,
                "Primary_Products": "Metal Components, Industrial Equipment, Machinery Parts",
                "Credit_Rating": "A-",
                "Risk_Level": "Low",
                "Market_Outlook": "Positive",
                "Revenue_2024": 122.16,
                "Net_Profit_2024": 18.10,
                "Profit_Margin": 14.82,
                "Growth_Rate": 27.3
            },
            {
                "Company_ID": "MSME002", 
                "Company_Name": "Minimac Systems Pvt Ltd",
                "Sector": "Manufacturing",
                "Location": "Coimbatore, Tamil Nadu", 
                "Founded_Year": 2002,
                "Employee_Count": 67,
                "Primary_Products": "Industrial Equipment, Precision Parts, Machine Tools",
                "Credit_Rating": "B-",
                "Risk_Level": "Medium-High", 
                "Market_Outlook": "Positive",
                "Revenue_2024": 26.53,
                "Net_Profit_2024": 3.31,
                "Profit_Margin": 12.48,
                "Growth_Rate": 25.3
            },
            {
                "Company_ID": "MSME003",
                "Company_Name": "Assam Carbon Products Ltd",
                "Sector": "Manufacturing", 
                "Location": "Hyderabad, Telangana",
                "Founded_Year": 2018,
                "Employee_Count": 36,
                "Primary_Products": "Machinery Parts, Precision Parts, Tools & Dies",
                "Credit_Rating": "A-",
                "Risk_Level": "Low",
                "Market_Outlook": "Positive", 
                "Revenue_2024": 45.78,
                "Net_Profit_2024": 7.89,
                "Profit_Margin": 17.24,
                "Growth_Rate": 35.8
            },
            {
                "Company_ID": "MSME011",
                "Company_Name": "Suguna Foods Pvt Ltd",
                "Sector": "Food Processing",
                "Location": "Coimbatore, Tamil Nadu",
                "Founded_Year": 1984,
                "Employee_Count": 125,
                "Primary_Products": "Poultry Products, Processed Foods, Frozen Foods", 
                "Credit_Rating": "A",
                "Risk_Level": "Low",
                "Market_Outlook": "Very Positive",
                "Revenue_2024": 189.45,
                "Net_Profit_2024": 35.67,
                "Profit_Margin": 18.83,
                "Growth_Rate": 42.1
            },
            {
                "Company_ID": "MSME012",
                "Company_Name": "MTR Foods Pvt Ltd", 
                "Sector": "Food Processing",
                "Location": "Bengaluru, Karnataka",
                "Founded_Year": 1924,
                "Employee_Count": 234,
                "Primary_Products": "Ready-to-Eat Foods, Spices, Traditional Foods",
                "Credit_Rating": "A+",
                "Risk_Level": "Low", 
                "Market_Outlook": "Very Positive",
                "Revenue_2024": 156.78,
                "Net_Profit_2024": 28.45,
                "Profit_Margin": 18.15,
                "Growth_Rate": 31.2
            },
            {
                "Company_ID": "MSME021",
                "Company_Name": "Imprezz Digital Solutions Pvt Ltd",
                "Sector": "Technology",
                "Location": "Pune, Maharashtra", 
                "Founded_Year": 2015,
                "Employee_Count": 45,
                "Primary_Products": "Web Development, Mobile Apps, Digital Marketing",
                "Credit_Rating": "B+",
                "Risk_Level": "Medium",
                "Market_Outlook": "Very Positive",
                "Revenue_2024": 23.45,
                "Net_Profit_2024": 6.78,
                "Profit_Margin": 28.91,
                "Growth_Rate": 67.3
            },
            {
                "Company_ID": "MSME031", 
                "Company_Name": "Core Healthcare Ltd",
                "Sector": "Healthcare",
                "Location": "Mumbai, Maharashtra",
                "Founded_Year": 2008,
                "Employee_Count": 89,
                "Primary_Products": "Medical Devices, Diagnostic Equipment, Healthcare IT",
                "Credit_Rating": "A-",
                "Risk_Level": "Low",
                "Market_Outlook": "Very Positive",
                "Revenue_2024": 145.67,
                "Net_Profit_2024": 41.23,
                "Profit_Margin": 28.31,
                "Growth_Rate": 58.9
            },
            {
                "Company_ID": "MSME041",
                "Company_Name": "Sutlej Textiles Ltd", 
                "Sector": "Textiles",
                "Location": "Ludhiana, Punjab", 
                "Founded_Year": 1986,
                "Employee_Count": 156,
                "Primary_Products": "Cotton Fabrics, Denim, Technical Textiles",
                "Credit_Rating": "A-",
                "Risk_Level": "Medium",
                "Market_Outlook": "Positive",
                "Revenue_2024": 98.45,
                "Net_Profit_2024": 12.67,
                "Profit_Margin": 12.87,
                "Growth_Rate": 22.4
            }
        ];

        this.news = [
            {
                "title": "Indian Manufacturing PMI Hits 8-Month High in September 2025",
                "summary": "India's manufacturing sector showed strong growth with PMI reaching 56.2, driven by increased domestic and export orders.",
                "sector": "Manufacturing", 
                "source": "Economic Times",
                "date": "2025-10-01",
                "sentiment": "positive"
            },
            {
                "title": "Food Processing Industry Expected to Reach $535 Billion by 2025-26", 
                "summary": "The food processing sector is witnessing robust growth driven by changing consumer preferences and government initiatives.",
                "sector": "Food Processing",
                "source": "Business Standard", 
                "date": "2025-09-28",
                "sentiment": "positive"
            },
            {
                "title": "Healthcare Technology Adoption Accelerates in Indian SMEs",
                "summary": "Small and medium healthcare enterprises are rapidly adopting digital technologies to improve patient care and operational efficiency.",
                "sector": "Healthcare",
                "source": "LiveMint",
                "date": "2025-09-30", 
                "sentiment": "positive"
            },
            {
                "title": "Textile Exports Face Headwinds Due to Global Economic Slowdown",
                "summary": "Indian textile exporters are experiencing challenges due to reduced global demand and supply chain disruptions.",
                "sector": "Textiles",
                "source": "Financial Express",
                "date": "2025-09-29",
                "sentiment": "negative" 
            },
            {
                "title": "Government Launches New Digital India Initiative for MSMEs",
                "summary": "New ₹10,000 crore digital transformation fund announced to help MSMEs adopt Industry 4.0 technologies.",
                "sector": "Technology",
                "source": "The Hindu BusinessLine",
                "date": "2025-10-02",
                "sentiment": "positive"
            },
            {
                "title": "Stock Market Volatility Affects MSME Funding",
                "summary": "Recent market fluctuations have made investors cautious about funding small and medium enterprises, leading to tighter credit conditions.",
                "sector": "General",
                "source": "Financial Times",
                "date": "2025-10-03",
                "sentiment": "negative"
            },
            {
                "title": "MSME Export Credit Scheme Extended for Another Year",
                "summary": "Government extends the export credit guarantee scheme helping MSMEs access international markets with better financing options.",
                "sector": "General",
                "source": "Business Today",
                "date": "2025-10-04",
                "sentiment": "positive"
            }
        ];

        this.stockData = {
            "NIFTY_MSME": { "value": 4567.89, "change": "+2.34%", "trend": "up" },
            "BSE_SME": { "value": 1234.56, "change": "-0.87%", "trend": "down" },
            "MANUFACTURING_INDEX": { "value": 2890.45, "change": "+1.67%", "trend": "up" },
            "HEALTHCARE_INDEX": { "value": 3456.78, "change": "+3.21%", "trend": "up" }
        };

        this.currentTab = 'chat';
        this.chatHistory = [];
        this.charts = {};
        
        this.initializeApp();
    }

    initializeApp() {
        this.setupTabNavigation();
        this.setupChatInterface();
        this.setupNewsFilter();
        this.setupDataExplorer();
        this.renderCompanies();
        this.renderNews();
        this.updateHeaderStats();
    }

    setupTabNavigation() {
        const tabButtons = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        tabButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const targetTab = btn.dataset.tab;
                
                // Update active states
                tabButtons.forEach(b => b.classList.remove('active'));
                tabContents.forEach(c => c.classList.remove('active'));
                
                btn.classList.add('active');
                const targetContent = document.getElementById(`${targetTab}-tab`);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
                
                this.currentTab = targetTab;
                
                // Initialize dashboard charts when switching to dashboard
                if (targetTab === 'dashboard') {
                    setTimeout(() => this.initializeCharts(), 100);
                }
            });
        });
    }

    setupChatInterface() {
        const chatInput = document.getElementById('chat-input');
        const sendBtn = document.getElementById('send-btn');
        const clearBtn = document.getElementById('clear-chat');
        const quickButtons = document.querySelectorAll('.quick-btn');

        const sendMessage = () => {
            const message = chatInput.value.trim();
            if (message) {
                this.handleUserMessage(message);
                chatInput.value = '';
            }
        };

        if (sendBtn) {
            sendBtn.addEventListener('click', sendMessage);
        }
        
        if (chatInput) {
            chatInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
        }

        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                this.chatHistory = [];
                const messagesContainer = document.getElementById('chat-messages');
                if (messagesContainer) {
                    messagesContainer.innerHTML = `
                        <div class="message ai-message">
                            <div class="message-content">
                                <strong>🤖 MSME AI Assistant</strong>
                                <p>Welcome! I'm your MSME Market Intelligence assistant. I can help you analyze company data, sector trends, financial performance, and market insights. Ask me anything about the companies in our database!</p>
                            </div>
                        </div>
                    `;
                }
            });
        }

        quickButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const query = btn.dataset.query;
                this.handleUserMessage(query);
            });
        });
    }

    async handleUserMessage(message) {
        // Add user message to chat
        this.addMessage(message, 'user');
        
        // Show thinking indicator
        this.showThinkingIndicator();
        
        // Simulate processing delay and generate response
        setTimeout(() => {
            this.hideThinkingIndicator();
            const response = this.generateRAGResponse(message);
            this.addMessage(response, 'ai');
        }, 1000);
    }

    addMessage(content, sender) {
        const messagesContainer = document.getElementById('chat-messages');
        if (!messagesContainer) return;
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`;
        
        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        if (sender === 'user') {
            contentDiv.innerHTML = `<p>${content}</p>`;
        } else {
            contentDiv.innerHTML = content;
        }
        
        messageDiv.appendChild(contentDiv);
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        this.chatHistory.push({ sender, content });
    }

    showThinkingIndicator() {
        const messagesContainer = document.getElementById('chat-messages');
        if (!messagesContainer) return;
        
        const thinkingDiv = document.createElement('div');
        thinkingDiv.className = 'message ai-message';
        thinkingDiv.id = 'thinking-indicator';
        thinkingDiv.innerHTML = `
            <div class="message-content">
                <div class="typing-indicator">
                    <span>🤖 Analyzing data</span>
                    <div class="typing-dots">
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                        <span class="typing-dot"></span>
                    </div>
                </div>
            </div>
        `;
        messagesContainer.appendChild(thinkingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    hideThinkingIndicator() {
        const indicator = document.getElementById('thinking-indicator');
        if (indicator) {
            indicator.remove();
        }
    }

    generateRAGResponse(query) {
        const lowerQuery = query.toLowerCase();
        
        // Manufacturing sector queries
        if (lowerQuery.includes('manufacturing') || lowerQuery.includes('manufacturing companies')) {
            const mfgCompanies = this.companies.filter(c => c.Sector === 'Manufacturing');
            const avgRevenue = mfgCompanies.reduce((sum, c) => sum + c.Revenue_2024, 0) / mfgCompanies.length;
            const avgGrowth = mfgCompanies.reduce((sum, c) => sum + c.Growth_Rate, 0) / mfgCompanies.length;
            
            return `
                <strong>🏭 Manufacturing Sector Analysis</strong>
                <p>I found ${mfgCompanies.length} manufacturing companies in our database:</p>
                <div class="data-highlight">
                    <div class="company-list">
                        ${mfgCompanies.map(c => `
                            <div class="company-item">
                                <strong>${c.Company_Name}</strong> - Revenue: ₹${c.Revenue_2024}M, Growth: ${c.Growth_Rate}%
                                <br><small>Location: ${c.Location} | Risk: ${c.Risk_Level}</small>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <p><strong>Key Insights:</strong></p>
                <ul>
                    <li>Average Revenue: ₹${avgRevenue.toFixed(1)}M</li>
                    <li>Average Growth Rate: ${avgGrowth.toFixed(1)}%</li>
                    <li>Sector Outlook: Most companies show positive market outlook</li>
                    <li>Recent News: Manufacturing PMI hit 8-month high at 56.2</li>
                </ul>
            `;
        }
        
        // Healthcare sector queries
        if (lowerQuery.includes('healthcare') || lowerQuery.includes('healthcare sector')) {
            const healthCompanies = this.companies.filter(c => c.Sector === 'Healthcare');
            
            return `
                <strong>🏥 Healthcare Sector Performance</strong>
                <p>Healthcare sector analysis from our MSME database:</p>
                <div class="data-highlight">
                    <div class="company-list">
                        ${healthCompanies.map(c => `
                            <div class="company-item">
                                <strong>${c.Company_Name}</strong>
                                <br>Revenue: ₹${c.Revenue_2024}M | Growth: ${c.Growth_Rate}% | Margin: ${c.Profit_Margin}%
                                <br><small>Products: ${c.Primary_Products}</small>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <p><strong>Sector Highlights:</strong></p>
                <ul>
                    <li>Exceptional growth rate of 58.9% (Core Healthcare Ltd)</li>
                    <li>High profit margins averaging 28.31%</li>
                    <li>Strong market outlook with technology adoption</li>
                    <li>Focus on medical devices and healthcare IT</li>
                </ul>
                <p>📈 <strong>Stock Update:</strong> Healthcare Index: ${this.stockData.HEALTHCARE_INDEX.value} (${this.stockData.HEALTHCARE_INDEX.change})</p>
            `;
        }
        
        // Technology comparison queries
        if (lowerQuery.includes('technology') || lowerQuery.includes('tech comparison')) {
            const techCompanies = this.companies.filter(c => c.Sector === 'Technology');
            
            return `
                <strong>💻 Technology Sector Comparison</strong>
                <p>Technology sector analysis and comparison:</p>
                <div class="data-highlight">
                    ${techCompanies.map(c => `
                        <div class="company-item">
                            <strong>${c.Company_Name}</strong>
                            <br>📍 ${c.Location} | Founded: ${c.Founded_Year}
                            <br>💰 Revenue: ₹${c.Revenue_2024}M | 📈 Growth: ${c.Growth_Rate}%
                            <br>🎯 Products: ${c.Primary_Products}
                            <br>⚡ Profit Margin: ${c.Profit_Margin}% | Risk: ${c.Risk_Level}
                        </div>
                    `).join('')}
                </div>
                <p><strong>Key Observations:</strong></p>
                <ul>
                    <li>Impressive 67.3% growth rate despite smaller size</li>
                    <li>Highest profit margins in our database at 28.91%</li>
                    <li>Government support with ₹10,000 crore digital transformation fund</li>
                    <li>Focus on web development and digital marketing</li>
                </ul>
            `;
        }
        
        // Food processing trends
        if (lowerQuery.includes('food processing') || lowerQuery.includes('food') || lowerQuery.includes('trends')) {
            const foodCompanies = this.companies.filter(c => c.Sector === 'Food Processing');
            
            return `
                <strong>🍽️ Food Processing Industry Trends</strong>
                <p>Latest trends and analysis of food processing companies:</p>
                <div class="data-highlight">
                    <div class="company-list">
                        ${foodCompanies.map(c => `
                            <div class="company-item">
                                <strong>${c.Company_Name}</strong>
                                <br>Est. ${c.Founded_Year} | Employees: ${c.Employee_Count}
                                <br>💰 ₹${c.Revenue_2024}M revenue | 📈 ${c.Growth_Rate}% growth
                                <br>🏆 Credit Rating: ${c.Credit_Rating}
                            </div>
                        `).join('')}
                    </div>
                </div>
                <p><strong>Industry Trends:</strong></p>
                <ul>
                    <li>Industry expected to reach $535 billion by 2025-26</li>
                    <li>Strong growth in ready-to-eat and processed foods</li>
                    <li>MTR Foods (est. 1924) showing 31.2% growth despite maturity</li>
                    <li>Suguna Foods leading with 42.1% growth rate</li>
                    <li>Average profit margin: 18.5% across the sector</li>
                </ul>
            `;
        }
        
        // Risk analysis queries
        if (lowerQuery.includes('risk') || lowerQuery.includes('risk analysis')) {
            const riskAnalysis = this.analyzeRiskByCompany();
            
            return `
                <strong>⚠️ Risk Analysis Across Sectors</strong>
                <p>Comprehensive risk assessment of companies in our database:</p>
                <div class="data-highlight">
                    <h4>Low Risk Companies (${riskAnalysis.low.length}):</h4>
                    ${riskAnalysis.low.map(c => `
                        <div class="company-item">
                            <strong>${c.Company_Name}</strong> (${c.Sector})
                            <br>Credit Rating: ${c.Credit_Rating} | Revenue: ₹${c.Revenue_2024}M
                        </div>
                    `).join('')}
                    
                    <h4>Medium Risk Companies (${riskAnalysis.medium.length}):</h4>
                    ${riskAnalysis.medium.map(c => `
                        <div class="company-item">
                            <strong>${c.Company_Name}</strong> (${c.Sector})
                            <br>Credit Rating: ${c.Credit_Rating} | Revenue: ₹${c.Revenue_2024}M
                        </div>
                    `).join('')}
                    
                    <h4>High Risk Companies (${riskAnalysis.high.length}):</h4>
                    ${riskAnalysis.high.map(c => `
                        <div class="company-item">
                            <strong>${c.Company_Name}</strong> (${c.Sector})
                            <br>Credit Rating: ${c.Credit_Rating} | Revenue: ₹${c.Revenue_2024}M
                        </div>
                    `).join('')}
                </div>
                <p><strong>Risk Insights:</strong></p>
                <ul>
                    <li>75% of companies classified as low risk</li>
                    <li>Food processing and healthcare sectors show lowest risk</li>
                    <li>Technology sector has medium risk due to market volatility</li>
                    <li>Recent market volatility affecting MSME funding</li>
                </ul>
            `;
        }
        
        // High growth companies
        if (lowerQuery.includes('high growth') || lowerQuery.includes('growth')) {
            const sortedByGrowth = [...this.companies].sort((a, b) => b.Growth_Rate - a.Growth_Rate).slice(0, 5);
            
            return `
                <strong>📈 High Growth Companies</strong>
                <p>Top performing companies by growth rate:</p>
                <div class="data-highlight">
                    <div class="company-list">
                        ${sortedByGrowth.map((c, index) => `
                            <div class="company-item">
                                <strong>#${index + 1} ${c.Company_Name}</strong>
                                <br>🚀 Growth Rate: ${c.Growth_Rate}% | Sector: ${c.Sector}
                                <br>💰 Revenue: ₹${c.Revenue_2024}M | Margin: ${c.Profit_Margin}%
                                <br>📍 ${c.Location} | Risk: ${c.Risk_Level}
                            </div>
                        `).join('')}
                    </div>
                </div>
                <p><strong>Growth Analysis:</strong></p>
                <ul>
                    <li>Technology leads with 67.3% growth (Imprezz Digital)</li>
                    <li>Healthcare shows strong 58.9% growth (Core Healthcare)</li>
                    <li>Food processing sector demonstrating solid growth</li>
                    <li>Average growth rate across top performers: ${(sortedByGrowth.reduce((sum, c) => sum + c.Growth_Rate, 0) / 5).toFixed(1)}%</li>
                </ul>
            `;
        }
        
        // Stock market and financial queries
        if (lowerQuery.includes('stock') || lowerQuery.includes('market') || lowerQuery.includes('financial')) {
            return `
                <strong>📊 Stock Market & Financial Overview</strong>
                <p>Current market indicators and financial performance:</p>
                <div class="data-highlight">
                    <h4>📈 Key Market Indices:</h4>
                    <div class="company-list">
                        <div class="company-item">
                            <strong>NIFTY MSME Index:</strong> ${this.stockData.NIFTY_MSME.value} (${this.stockData.NIFTY_MSME.change})
                        </div>
                        <div class="company-item">
                            <strong>BSE SME Index:</strong> ${this.stockData.BSE_SME.value} (${this.stockData.BSE_SME.change})
                        </div>
                        <div class="company-item">
                            <strong>Manufacturing Index:</strong> ${this.stockData.MANUFACTURING_INDEX.value} (${this.stockData.MANUFACTURING_INDEX.change})
                        </div>
                        <div class="company-item">
                            <strong>Healthcare Index:</strong> ${this.stockData.HEALTHCARE_INDEX.value} (${this.stockData.HEALTHCARE_INDEX.change})
                        </div>
                    </div>
                </div>
                <p><strong>Financial Highlights:</strong></p>
                <ul>
                    <li>Total portfolio revenue: ₹${this.companies.reduce((sum, c) => sum + c.Revenue_2024, 0).toFixed(1)}M</li>
                    <li>Average profit margin: ${(this.companies.reduce((sum, c) => sum + c.Profit_Margin, 0) / this.companies.length).toFixed(1)}%</li>
                    <li>Market volatility affecting MSME funding conditions</li>
                    <li>Export credit scheme extended for better financing</li>
                </ul>
            `;
        }
        
        // General sector comparison
        if (lowerQuery.includes('sector') || lowerQuery.includes('compare sectors')) {
            return this.generateSectorComparison();
        }
        
        // Default response with general overview
        return `
            <strong>🤖 MSME Market Intelligence Overview</strong>
            <p>I can help you with various analyses. Here's what I can do:</p>
            <ul>
                <li>🏭 <strong>Sector Analysis:</strong> Manufacturing, Healthcare, Technology, Food Processing, Textiles</li>
                <li>📊 <strong>Financial Performance:</strong> Revenue trends, profit margins, growth rates</li>
                <li>⚠️ <strong>Risk Assessment:</strong> Credit ratings, risk levels, market outlook</li>
                <li>📈 <strong>Market Data:</strong> Stock indices, growth companies, trends</li>
                <li>📰 <strong>News Integration:</strong> Latest industry developments</li>
            </ul>
            <p>Try asking: "Show me healthcare companies" or "Compare technology sector performance" or "Risk analysis by sector"</p>
            <div class="data-highlight">
                <strong>Quick Stats:</strong> ${this.companies.length} companies tracked | Avg Growth: ${(this.companies.reduce((sum, c) => sum + c.Growth_Rate, 0) / this.companies.length).toFixed(1)}% | Total Revenue: ₹${this.companies.reduce((sum, c) => sum + c.Revenue_2024, 0).toFixed(1)}M
            </div>
        `;
    }

    analyzeRiskByCompany() {
        return {
            low: this.companies.filter(c => c.Risk_Level === 'Low'),
            medium: this.companies.filter(c => c.Risk_Level === 'Medium'),
            high: this.companies.filter(c => c.Risk_Level.includes('High'))
        };
    }

    generateSectorComparison() {
        const sectorStats = {};
        this.companies.forEach(company => {
            if (!sectorStats[company.Sector]) {
                sectorStats[company.Sector] = {
                    count: 0,
                    totalRevenue: 0,
                    totalGrowth: 0,
                    totalMargin: 0,
                    companies: []
                };
            }
            sectorStats[company.Sector].count++;
            sectorStats[company.Sector].totalRevenue += company.Revenue_2024;
            sectorStats[company.Sector].totalGrowth += company.Growth_Rate;
            sectorStats[company.Sector].totalMargin += company.Profit_Margin;
            sectorStats[company.Sector].companies.push(company);
        });

        let comparison = `
            <strong>🔍 Comprehensive Sector Comparison</strong>
            <p>Detailed analysis across all sectors in our database:</p>
            <div class="data-highlight">
        `;

        Object.keys(sectorStats).forEach(sector => {
            const stats = sectorStats[sector];
            const avgRevenue = stats.totalRevenue / stats.count;
            const avgGrowth = stats.totalGrowth / stats.count;
            const avgMargin = stats.totalMargin / stats.count;

            comparison += `
                <div class="company-item">
                    <strong>${sector} Sector</strong>
                    <br>Companies: ${stats.count} | Avg Revenue: ₹${avgRevenue.toFixed(1)}M
                    <br>Avg Growth: ${avgGrowth.toFixed(1)}% | Avg Margin: ${avgMargin.toFixed(1)}%
                </div>
            `;
        });

        comparison += `
            </div>
            <p><strong>Sector Rankings by Growth:</strong></p>
            <ol>
        `;

        const sortedSectors = Object.keys(sectorStats).sort((a, b) => 
            (sectorStats[b].totalGrowth / sectorStats[b].count) - (sectorStats[a].totalGrowth / sectorStats[a].count)
        );

        sortedSectors.forEach(sector => {
            const avgGrowth = (sectorStats[sector].totalGrowth / sectorStats[sector].count).toFixed(1);
            comparison += `<li>${sector}: ${avgGrowth}% average growth</li>`;
        });

        comparison += `</ol>`;

        return comparison;
    }

    initializeCharts() {
        this.createSectorChart();
        this.createRevenueChart();
        this.createGrowthChart();
    }

    createSectorChart() {
        const ctx = document.getElementById('sector-chart');
        if (!ctx) return;

        const sectorCounts = {};
        this.companies.forEach(c => {
            sectorCounts[c.Sector] = (sectorCounts[c.Sector] || 0) + 1;
        });

        if (this.charts.sectorChart) {
            this.charts.sectorChart.destroy();
        }

        this.charts.sectorChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: Object.keys(sectorCounts),
                datasets: [{
                    data: Object.values(sectorCounts),
                    backgroundColor: ['#1FB8CD', '#FFC185', '#B4413C', '#ECEBD5', '#5D878F']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
    }

    createRevenueChart() {
        const ctx = document.getElementById('revenue-chart');
        if (!ctx) return;

        const sectorRevenue = {};
        this.companies.forEach(c => {
            if (!sectorRevenue[c.Sector]) sectorRevenue[c.Sector] = 0;
            sectorRevenue[c.Sector] += c.Revenue_2024;
        });

        if (this.charts.revenueChart) {
            this.charts.revenueChart.destroy();
        }

        this.charts.revenueChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: Object.keys(sectorRevenue),
                datasets: [{
                    label: 'Revenue (₹M)',
                    data: Object.values(sectorRevenue),
                    backgroundColor: ['#1FB8CD', '#FFC185', '#B4413C', '#ECEBD5', '#5D878F']
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    createGrowthChart() {
        const ctx = document.getElementById('growth-chart');
        if (!ctx) return;

        const sectorGrowth = {};
        const sectorCounts = {};
        
        this.companies.forEach(c => {
            if (!sectorGrowth[c.Sector]) {
                sectorGrowth[c.Sector] = 0;
                sectorCounts[c.Sector] = 0;
            }
            sectorGrowth[c.Sector] += c.Growth_Rate;
            sectorCounts[c.Sector]++;
        });

        // Calculate averages
        Object.keys(sectorGrowth).forEach(sector => {
            sectorGrowth[sector] = sectorGrowth[sector] / sectorCounts[sector];
        });

        if (this.charts.growthChart) {
            this.charts.growthChart.destroy();
        }

        this.charts.growthChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: Object.keys(sectorGrowth),
                datasets: [{
                    label: 'Average Growth Rate (%)',
                    data: Object.values(sectorGrowth),
                    borderColor: '#1FB8CD',
                    backgroundColor: 'rgba(31, 184, 205, 0.1)',
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    setupNewsFilter() {
        const sectorFilter = document.getElementById('sector-filter');
        if (sectorFilter) {
            sectorFilter.addEventListener('change', () => {
                this.renderNews(sectorFilter.value);
            });
        }
    }

    renderNews(filterSector = '') {
        const newsFeed = document.getElementById('news-feed');
        if (!newsFeed) return;
        
        const filteredNews = filterSector ? 
            this.news.filter(article => article.sector === filterSector) : 
            this.news;

        newsFeed.innerHTML = filteredNews.map(article => `
            <article class="news-article">
                <div class="news-meta">
                    <span class="news-sector ${article.sector.replace(' ', '.')}">${article.sector}</span>
                    <span class="news-date">${new Date(article.date).toLocaleDateString()}</span>
                </div>
                <h3 class="news-title">${article.title}</h3>
                <p class="news-summary">${article.summary}</p>
                <div class="news-footer">
                    <span class="news-source">${article.source}</span>
                    <span class="sentiment-indicator sentiment-${article.sentiment}">
                        ${article.sentiment.charAt(0).toUpperCase() + article.sentiment.slice(1)}
                    </span>
                </div>
            </article>
        `).join('');
    }

    setupDataExplorer() {
        const searchInput = document.getElementById('search-input');
        const sectorFilter = document.getElementById('sector-filter-explorer');
        const riskFilter = document.getElementById('risk-filter');

        const filterCompanies = () => {
            const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
            const selectedSector = sectorFilter ? sectorFilter.value : '';
            const selectedRisk = riskFilter ? riskFilter.value : '';

            let filtered = this.companies.filter(company => {
                const matchesSearch = company.Company_Name.toLowerCase().includes(searchTerm) ||
                                    company.Location.toLowerCase().includes(searchTerm) ||
                                    company.Primary_Products.toLowerCase().includes(searchTerm);
                const matchesSector = !selectedSector || company.Sector === selectedSector;
                const matchesRisk = !selectedRisk || company.Risk_Level === selectedRisk;
                
                return matchesSearch && matchesSector && matchesRisk;
            });

            this.renderCompanies(filtered);
        };

        if (searchInput) {
            searchInput.addEventListener('input', filterCompanies);
        }
        if (sectorFilter) {
            sectorFilter.addEventListener('change', filterCompanies);
        }
        if (riskFilter) {
            riskFilter.addEventListener('change', filterCompanies);
        }
    }

    renderCompanies(companiesToRender = this.companies) {
        const companiesGrid = document.getElementById('companies-grid');
        if (!companiesGrid) return;
        
        companiesGrid.innerHTML = companiesToRender.map(company => `
            <div class="company-card">
                <div class="company-header">
                    <h3 class="company-name">${company.Company_Name}</h3>
                    <span class="company-sector">${company.Sector}</span>
                </div>
                <p class="company-location">📍 ${company.Location}</p>
                <div class="company-metrics">
                    <div class="metric">
                        <span class="metric-value">₹${company.Revenue_2024}M</span>
                        <span class="metric-label">Revenue</span>
                    </div>
                    <div class="metric">
                        <span class="metric-value">${company.Growth_Rate}%</span>
                        <span class="metric-label">Growth</span>
                    </div>
                    <div class="metric">
                        <span class="metric-value">${company.Profit_Margin}%</span>
                        <span class="metric-label">Margin</span>
                    </div>
                    <div class="metric">
                        <span class="metric-value">${company.Employee_Count}</span>
                        <span class="metric-label">Employees</span>
                    </div>
                </div>
                <p><strong>Products:</strong> ${company.Primary_Products}</p>
                <div class="company-footer">
                    <span class="credit-rating">Rating: ${company.Credit_Rating}</span>
                    <span class="risk-level risk-${company.Risk_Level.toLowerCase().replace('-', '')}">${company.Risk_Level}</span>
                </div>
            </div>
        `).join('');
    }

    updateHeaderStats() {
        const totalRevenue = this.companies.reduce((sum, c) => sum + c.Revenue_2024, 0);
        const avgGrowth = this.companies.reduce((sum, c) => sum + c.Growth_Rate, 0) / this.companies.length;
        
        const totalCompaniesEl = document.getElementById('total-companies');
        const avgGrowthEl = document.getElementById('avg-growth');
        const marketCapEl = document.getElementById('market-cap');
        
        if (totalCompaniesEl) totalCompaniesEl.textContent = this.companies.length;
        if (avgGrowthEl) avgGrowthEl.textContent = `${avgGrowth.toFixed(1)}%`;
        if (marketCapEl) marketCapEl.textContent = `₹${(totalRevenue / 1000).toFixed(1)}B`;
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.msmeApp = new MSMEIntelligenceApp();
});