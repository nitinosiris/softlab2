# Personal Finance AI Assistant - Use Case Diagram

## System Overview
```mermaid
graph TB
    subgraph "Personal Finance AI Assistant System"
        subgraph "Core MVP Features"
            UC1[Account Linking & Data Sync]
            UC2[Conversational AI Interface]
            UC3[Financial Dashboard]
            UC4[Goals & Projections]
            UC5[Financial Health Analysis]
            UC6[Insights & Recommendations]
            UC7[Data Export & Privacy]
        end
        
        subgraph "Advanced Features"
            UC8[Visual Analytics]
            UC9[Anomaly Detection]
            UC10[Financial Nudges]
        end
        
        subgraph "Background Services"
            UC11[Data Synchronization]
            UC12[AI Processing]
            UC13[Security Management]
        end
    end
    
    %% Actors
    User[👤 End User]
    Admin[👨‍💼 System Admin]
    FinInst[🏦 Financial Institutions]
    AIService[🤖 Gemini AI Service]
    MCPService[🔗 Fi MCP Service]
    
    %% User relationships
    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    User --> UC6
    User --> UC7
    User --> UC8
    User --> UC9
    User --> UC10
    
    %% Admin relationships
    Admin --> UC13
    Admin --> UC11
    
    %% External service relationships
    FinInst --> UC1
    AIService --> UC2
    AIService --> UC4
    AIService --> UC5
    AIService --> UC6
    MCPService --> UC1
    MCPService --> UC11
```

## Detailed Use Case Descriptions

### 1. Account Linking & Data Sync
```mermaid
graph LR
    User[👤 User] --> UC1_1[Connect Bank Account]
    User --> UC1_2[Link Mutual Fund Account]
    User --> UC1_3[Add Credit Card]
    User --> UC1_4[Connect EPF Account]
    User --> UC1_5[Link Loan Account]
    User --> UC1_6[Manage Account Permissions]
    User --> UC1_7[Remove Account Connection]
    
    UC1_1 --> MCPService[🔗 Fi MCP]
    UC1_2 --> MCPService
    UC1_3 --> MCPService
    UC1_4 --> MCPService
    UC1_5 --> MCPService
    
    MCPService --> FinInst[🏦 Financial Institutions]
```

### 2. Conversational AI Interface
```mermaid
graph LR
    User[👤 User] --> UC2_1[Ask Financial Question]
    User --> UC2_2[Request Spending Analysis]
    User --> UC2_3[Query Net Worth]
    User --> UC2_4[Ask Investment Advice]
    User --> UC2_5[Check Loan Affordability]
    User --> UC2_6[Get Budget Insights]
    
    UC2_1 --> AIService[🤖 Gemini AI]
    UC2_2 --> AIService
    UC2_3 --> AIService
    UC2_4 --> AIService
    UC2_5 --> AIService
    UC2_6 --> AIService
```

### 3. Financial Dashboard
```mermaid
graph LR
    User[👤 User] --> UC3_1[View Net Worth]
    User --> UC3_2[Check Income vs Expenses]
    User --> UC3_3[Monitor Credit Score]
    User --> UC3_4[Review Investment Summary]
    User --> UC3_5[Track Asset Allocation]
    User --> UC3_6[View Liability Breakdown]
    User --> UC3_7[Customize Dashboard]
```

### 4. Goals & Projections
```mermaid
graph LR
    User[👤 User] --> UC4_1[Set Home Purchase Goal]
    User --> UC4_2[Plan Retirement Savings]
    User --> UC4_3[Create Education Fund]
    User --> UC4_4[Run What-If Simulations]
    User --> UC4_5[Track Goal Progress]
    User --> UC4_6[Modify Goal Parameters]
    User --> UC4_7[Compare Scenarios]
    
    UC4_4 --> AIService[🤖 Gemini AI]
    UC4_7 --> AIService
```

### 5. Financial Health Analysis
```mermaid
graph LR
    User[👤 User] --> UC5_1[Get Health Score]
    User --> UC5_2[Analyze Debt Ratio]
    User --> UC5_3[Check Emergency Fund]
    User --> UC5_4[Review Expense Patterns]
    User --> UC5_5[Assess Investment Risk]
    
    UC5_1 --> AIService[🤖 Gemini AI]
    UC5_2 --> AIService
    UC5_3 --> AIService
    UC5_4 --> AIService
    UC5_5 --> AIService
```

### 6. Insights & Recommendations
```mermaid
graph LR
    User[👤 User] --> UC6_1[Get Investment Suggestions]
    User --> UC6_2[Receive Debt Advice]
    User --> UC6_3[Budget Optimization Tips]
    User --> UC6_4[SIP Performance Review]
    User --> UC6_5[Tax Saving Recommendations]
    User --> UC6_6[Risk Assessment]
    
    UC6_1 --> AIService[🤖 Gemini AI]
    UC6_2 --> AIService
    UC6_3 --> AIService
    UC6_4 --> AIService
    UC6_5 --> AIService
    UC6_6 --> AIService
```

### 7. Data Privacy & Export
```mermaid
graph LR
    User[👤 User] --> UC7_1[Export PDF Report]
    User --> UC7_2[Download CSV Data]
    User --> UC7_3[Manage Data Permissions]
    User --> UC7_4[View Data Usage]
    User --> UC7_5[Delete Personal Data]
    User --> UC7_6[Share with Third Party]
    User --> UC7_7[API Data Access]
```

## Actor Definitions

### Primary Actors

**👤 End User (Primary Actor)**
- Individual seeking personal finance management
- Wants to understand financial health and make informed decisions
- Interacts with all core features of the system

**👨‍💼 System Administrator**
- Manages system configuration and security
- Monitors system performance and data integrity
- Handles user support and troubleshooting

### Secondary Actors

**🏦 Financial Institutions**
- Banks, mutual fund companies, credit card providers
- Provide financial data through APIs
- Maintain account information and transaction history

**🤖 Gemini AI Service**
- Google's AI service for natural language processing
- Generates insights and recommendations
- Processes complex financial queries

**🔗 Fi MCP (Model Context Protocol) Service**
- Secure data aggregation service
- Connects to multiple financial institutions
- Normalizes and standardizes financial data

## Use Case Priorities

### Core MVP (Must Have)
1. **Account Linking & Data Sync** - Foundation for all other features
2. **Conversational AI Interface** - Primary user interaction method
3. **Financial Dashboard** - Central information hub
4. **Goals & Projections** - Key value proposition
5. **Financial Health Analysis** - Core analytical feature
6. **Insights & Recommendations** - AI-driven value addition
7. **Data Privacy & Export** - Security and compliance

### Advanced Features (Should Have)
8. **Visual Analytics** - Enhanced user experience
9. **Anomaly Detection** - Proactive security
10. **Financial Nudges** - Behavioral improvement

### Supporting Services (Must Have for Operations)
11. **Data Synchronization** - Automated data updates
12. **AI Processing** - Backend intelligence
13. **Security Management** - System protection

## Key Use Case Relationships

```mermaid
graph TD
    UC1[Account Linking] --> UC3[Dashboard]
    UC1 --> UC5[Health Analysis]
    UC3 --> UC2[AI Chat]
    UC5 --> UC6[Recommendations]
    UC6 --> UC4[Goals & Projections]
    UC2 --> UC7[Data Export]
    UC11[Data Sync] --> UC1
    UC11 --> UC9[Anomaly Detection]
    UC12[AI Processing] --> UC2
    UC12 --> UC4
    UC12 --> UC5
    UC12 --> UC6
    UC13[Security] --> UC1
    UC13 --> UC7
```