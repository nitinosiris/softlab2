# Figma Conversion Guide - Personal Finance AI Assistant

## 🎨 Design System Setup

### 1. Create Base Design System in Figma

#### **Color Palette**
Create color styles in Figma:
- **Primary/500**: #2563EB (Blue)
- **Success/500**: #10B981 (Green) 
- **Warning/500**: #F59E0B (Amber)
- **Error/500**: #EF4444 (Red)
- **Gray/50**: #F8FAFC (Background)
- **Gray/800**: #1F2937 (Text)
- **Gray/300**: #D1D5DB (Borders)
- **White**: #FFFFFF

#### **Typography Styles**
```
Display/Large: Inter Bold, 32px, Line Height 40px
Heading/H1: Inter Bold, 24px, Line Height 32px
Heading/H2: Inter SemiBold, 20px, Line Height 28px
Body/Large: Inter Regular, 16px, Line Height 24px
Body/Regular: Inter Regular, 14px, Line Height 20px
Caption: Inter Regular, 12px, Line Height 16px
```

#### **Component Library Structure**
```
📁 Components
├── 🔵 Atoms
│   ├── Buttons (Primary, Secondary, Ghost)
│   ├── Input Fields
│   ├── Icons
│   └── Progress Bars
├── 🟡 Molecules  
│   ├── Cards
│   ├── Navigation Items
│   ├── Chat Bubbles
│   └── Goal Progress
└── 🟢 Organisms
    ├── Dashboard Header
    ├── Chat Interface
    ├── Goal Cards
    └── Account Lists
```

## 📱 Frame Setup

### **Desktop Frames (1440px width)**
1. **Landing Page**: 1440 × 1024px
2. **Dashboard**: 1440 × 1024px
3. **Chat Interface**: 1440 × 1024px
4. **Goals Page**: 1440 × 1024px
5. **Insights Page**: 1440 × 1024px

### **Mobile Frames (375px width)**
1. **Mobile Dashboard**: 375 × 812px
2. **Mobile Chat**: 375 × 812px
3. **Mobile Goals**: 375 × 812px

## 🔧 Component Creation Guide

### **1. Navigation Header Component**
```
Frame: 1440 × 80px
Background: White (#FFFFFF)
Border Bottom: 1px solid Gray/300

Elements:
- Logo: 32×32px icon + "FinanceAI" text (Heading/H2)
- Navigation: Dashboard, Goals, Chat, Insights (Body/Regular)
- User Avatar: 40×40px circle + dropdown icon
```

### **2. Dashboard Cards**
```
Net Worth Card:
- Frame: 680 × 120px
- Background: White with shadow (0px 4px 6px rgba(0,0,0,0.1))
- Border Radius: 12px
- Padding: 24px

Content:
- Title: "Net Worth" (Body/Large, Gray/800)
- Amount: "₹18,45,000" (Display/Large, Gray/800)
- Trend: "+2.3% this month" (Body/Regular, Success/500)
```

### **3. Goal Progress Component**
```
Goal Card:
- Frame: 680 × 140px
- Background: White
- Border Radius: 12px
- Padding: 20px

Elements:
- Icon: 24×24px (🏠)
- Title: "Home Purchase" (Heading/H2)
- Status Badge: Rounded rectangle with status color
- Progress Bar: 8px height, rounded, with percentage fill
- Details: Target amount, current progress (Body/Regular)
```

### **4. Chat Interface Components**
```
Chat Container:
- Frame: 800 × 600px
- Background: Gray/50
- Border Radius: 12px

Message Bubble (AI):
- Max width: 480px
- Background: White
- Border Radius: 16px 16px 16px 4px
- Padding: 12px 16px
- Shadow: 0px 2px 4px rgba(0,0,0,0.05)

Message Bubble (User):
- Max width: 480px  
- Background: Primary/500
- Color: White
- Border Radius: 16px 16px 4px 16px
- Padding: 12px 16px
```

## 📋 Step-by-Step Recreation Process

### **Phase 1: Setup (30 mins)**
1. Create new Figma file: "Personal Finance AI Assistant"
2. Set up design system (colors, typography, effects)
3. Create component library structure
4. Import icons (use Feather or Heroicons)

### **Phase 2: Components (2 hours)**
1. **Create Atomic Components:**
   - Buttons (3 variants: Primary, Secondary, Ghost)
   - Input fields with labels
   - Progress bars (3 sizes)
   - Status badges (4 colors)

2. **Build Molecular Components:**
   - Dashboard cards (4 variants)
   - Chat message bubbles (2 variants)
   - Navigation items
   - Goal progress cards

3. **Construct Organism Components:**
   - Full navigation header
   - Complete chat interface
   - Dashboard grid layout

### **Phase 3: Pages (3 hours)**

#### **Landing Page Recreation:**
```
Structure:
├── Header (Logo + CTA buttons)
├── Hero Section (Headline + Description + CTA)
├── Feature Cards (4 columns)
└── Footer (minimal)

Key Measurements:
- Header: Full width × 80px
- Hero: 600px width centered
- Feature Cards: 280px × 200px each
- Spacing: 80px vertical between sections
```

#### **Dashboard Recreation:**
```
Layout Grid:
├── Header (full width)
├── Welcome Section (full width)
├── Net Worth Card (680px)
├── 3-Column Cards Row
│   ├── Monthly Overview (320px)
│   ├── Investment Performance (320px)
│   └── Credit Score (320px)
└── Goals Section (full width)

Grid: 12 columns, 24px gutters
```

#### **Chat Interface Recreation:**
```
Layout:
├── Chat Header (title + clear button)
├── Messages Container (scrollable)
│   ├── AI Welcome Message
│   ├── User Question
│   ├── AI Response with breakdown
│   └── User Follow-up
├── Input Area (text field + send button)
└── Quick Actions (4 buttons)
```

## 🎨 Advanced Figma Techniques

### **1. Auto Layout Setup**
- Use Auto Layout for all cards and containers
- Set proper spacing (16px, 24px, 32px)
- Configure resizing behavior (Fill container vs Fixed)

### **2. Component Variants**
```
Button Component Variants:
- Property: Type (Primary, Secondary, Ghost)
- Property: Size (Large, Medium, Small)
- Property: State (Default, Hover, Disabled)
```

### **3. Interactive Prototyping**
```
Connections to Create:
- Landing → Dashboard (Sign Up flow)
- Dashboard → Chat (Navigation)
- Chat → Goals (From AI response)
- Goals → Goal Details (Click goal card)
- Goal Details → What-if Analysis
```

### **4. Design Tokens**
Create Figma variables for:
- Spacing scale (4, 8, 12, 16, 24, 32, 48, 64)
- Border radius (4, 8, 12, 16, 24)
- Shadow styles (sm, md, lg, xl)

## 📱 Mobile Adaptation

### **Responsive Breakpoints:**
- Desktop: 1440px
- Tablet: 768px  
- Mobile: 375px

### **Mobile-Specific Changes:**
1. **Navigation**: Convert to bottom tab bar
2. **Cards**: Stack vertically instead of grid
3. **Chat**: Full-screen overlay on mobile
4. **Text Sizes**: Reduce by 2px on mobile

## 🔄 Component States

### **Interactive States to Design:**
```
Buttons:
- Default
- Hover (slight background change)
- Active (pressed state)
- Disabled (50% opacity)

Cards:
- Default
- Hover (subtle shadow increase)
- Selected (border highlight)

Input Fields:
- Default
- Focus (border color change)
- Error (red border + message)
- Disabled
```

## 📊 Data Visualization

### **Charts to Create:**
1. **Progress Bars**: Animated, color-coded
2. **Donut Charts**: For asset allocation
3. **Line Charts**: For goal progress over time
4. **Bar Charts**: For expense categories

### **Chart Specifications:**
```
Progress Bar:
- Height: 8px
- Border Radius: 4px
- Background: Gray/200
- Fill: Success/500, Warning/500, or Error/500

Donut Chart:
- Size: 200×200px
- Stroke width: 16px
- Colors: Primary/500, Success/500, Warning/500
```

## 🎯 Figma Plugins to Use

### **Recommended Plugins:**
1. **Iconify**: For consistent icon system
2. **Content Reel**: For realistic financial data
3. **Figma to React**: For developer handoff
4. **Auto Layout**: For responsive design
5. **Chart**: For data visualization

### **Content Generation:**
- Use realistic Indian names and amounts
- Currency format: ₹1,25,000 (Indian comma style)
- Dates: DD MMM YYYY format
- Phone numbers: +91 format

## 📋 Figma File Organization

### **Page Structure:**
```
📄 Design System
├── Colors & Typography
├── Icons Library  
├── Component Library
└── Documentation

📄 Wireframes (Desktop)
├── 01. Landing Page
├── 02. Onboarding Flow
├── 03. Dashboard Overview
├── 04. Dashboard Detailed
├── 05. Chat Interface
├── 06. Goals Overview
├── 07. Goal Details
├── 08. Insights & Health
└── 09. Account Management

📄 Mobile Wireframes
├── Mobile Dashboard
├── Mobile Chat
└── Mobile Goals

📄 Prototypes
├── Desktop User Flow
└── Mobile User Flow
```

## 🚀 Export Specifications

### **For Development:**
- Export icons: SVG format
- Export images: 2x PNG for retina
- Color codes: HEX values
- Spacing: 8px grid system
- Typography: CSS specifications

### **Handoff Documentation:**
- Component specifications
- Interaction details
- Animation timings
- Responsive behavior notes

## ⏱️ Time Estimates

### **Total Time: ~8-10 hours**
- Design System Setup: 1 hour
- Component Creation: 3 hours  
- Page Recreation: 4 hours
- Mobile Adaptation: 1 hour
- Prototyping: 1 hour
- Polish & Documentation: 1 hour

## 🎯 Pro Tips for Figma

1. **Use consistent naming**: "Component/Variant/State"
2. **Group related elements**: Use frames and groups
3. **Layer organization**: Name all layers clearly
4. **Version control**: Save versions at major milestones
5. **Comments**: Add notes for developers
6. **Shared styles**: Use for all colors and text styles
7. **Component testing**: Test all variants work correctly
8. **Accessibility**: Ensure color contrast meets WCAG guidelines

This guide provides everything needed to recreate the wireframes in Figma with professional-quality components and proper organization.