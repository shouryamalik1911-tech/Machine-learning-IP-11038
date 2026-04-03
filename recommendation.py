def get_recommendations(career):
    """
    Returns recommendations based on the predicted career.
    Includes courses, skills, certifications, internships, projects, and a roadmap.
    """
    recommendations = {
        "Applications Developer": {
            "Courses": ["Advanced Java Programming", "Mobile App Development with Flutter", "Software Architecture Design"],
            "Skills": ["Java/Kotlin", "Swift", "API Integration", "UI/UX Design"],
            "Certifications": ["Google Associate Android Developer", "Oracle Certified Professional: Java SE Developer"],
            "Internships": ["Mobile App Intern", "Software Development Intern at a startup"],
            "Projects": ["Task Management App", "E-commerce System with Microservices"],
            "Roadmap": [
                "Master a core language (Java/Swift)",
                "Learn mobile/desktop frameworks",
                "Build and deploy a personal project to App Store/Play Store",
                "Apply for junior developer roles"
            ]
        },
        "CRM Technical Developer": {
            "Courses": ["Salesforce Administration", "Microsoft Dynamics 365 Development", "Cloud Computing Basics"],
            "Skills": ["Salesforce Apex", "Apex Web Services", "Database Management", "SQL"],
            "Certifications": ["Salesforce Platform Developer I", "Microsoft Certified: Dynamics 365 Fundamentals"],
            "Internships": ["CRM Intern", "Business Analyst Intern"],
            "Projects": ["Customer Portal for a local business", "Survey Automation System"],
            "Roadmap": [
                "Learn CRM platforms like Salesforce",
                "Understand customer relationship management workflows",
                "Get certified as a CRM Developer",
                "Apply to Enterprise IT consulting firms"
            ]
        },
        "Database Developer": {
            "Courses": ["Advanced SQL and Database Tuning", "NoSQL Databases (MongoDB/Cassandra)", "Data Warehousing"],
            "Skills": ["SQL", "PL/SQL", "MongoDB", "Data Modeling", "ETL Processes"],
            "Certifications": ["Oracle Database PL/SQL Developer Certified Professional", "MongoDB Certified Developer"],
            "Internships": ["Database Administration Intern", "Data Engineering Intern"],
            "Projects": ["Library Management System with Scalable Database", "Real-time Analytics Dashboard"],
            "Roadmap": [
                "Master SQL and relational database design",
                "Explore NoSQL and Big Data tools",
                "Work on data migration and optimization projects",
                "Become a Database Specialist"
            ]
        },
        "Mobile Applications Developer": {
            "Courses": ["Android Development with Kotlin", "iOS Development with Swift", "Cross-Platform with React Native"],
            "Skills": ["Kotlin/Swift", "React Native", "Firebase", "State Management (Redux/Provider)"],
            "Certifications": ["Associate Android Developer", "iOS App Development Certificate"],
            "Internships": ["Mobile Development Intern", "UI/UX Design Intern"],
            "Projects": ["Weather Forecast App", "Fitness Tracker with Real-time Data"],
            "Roadmap": [
                "Focus on either Android or iOS specialized track",
                "Build at least 3 apps with different features (API, Local Storage, Camera)",
                "Learn cross-platform development",
                "Work as a Mobile Dev"
            ]
        },
        "Network Security Engineer": {
            "Courses": ["Network Security Fundamentals", "Cisco Certified Network Associate (CCNA)", "Ethical Hacking"],
            "Skills": ["Networking (TCP/IP)", "Firewalls", "VPNs", "Intrusion Detection Systems"],
            "Certifications": ["CompTIA Security+", "Cisco CCNA Security", "CEH (Certified Ethical Hacker)"],
            "Internships": ["Network Admin Intern", "Security Operation Center (SOC) Intern"],
            "Projects": ["Secure Home Network Setup", "Small-scale Intrusion Detection System"],
            "Roadmap": [
                "Learn basics of Networking and Linux",
                "Gain hands-on experience with Cisco/Juniper hardware",
                "Obtain focus-based security certifications",
                "Join a cyber-security firm"
            ]
        },
        "Software Developer": {
            "Courses": ["Full Stack Web Development", "Design Patterns", "Algorithms and Data Structures"],
            "Skills": ["Python/JavaScript/C++", "Git/GitHub", "Problem Solving", "Unit Testing"],
            "Certifications": ["Microsoft Certified: Azure Developer Associate", "AWS Certified Developer – Associate"],
            "Internships": ["Backend Developer Intern", "General Software Engineering Intern"],
            "Projects": ["Open Source Contribution", "Full-stack Social Media Clone"],
            "Roadmap": [
                "Solidify Data Structures and Algorithms knowledge",
                "Learn a full-stack framework (MERN/Django)",
                "Contribute to open-source projects",
                "Land a Software Engineer role"
            ]
        },
        "Software Engineer": {
            "Courses": ["Distributed Systems", "Cloud Computing", "Software Testing and Quality Assurance"],
            "Skills": ["OOP", "System Design", "Cloud Services (AWS/Azure)", "Agile/Scrum"],
            "Certifications": ["CSEP (Certified Systems Engineering Professional)", "AWS Solutions Architect"],
            "Internships": ["Systems Engineering Intern", "Software Architect Intern"],
            "Projects": ["Inventory Management System", "Automated Testing Pipeline"],
            "Roadmap": [
                "Understand the full software development life cycle (SDLC)",
                "Master System Design principles",
                "Work on complex, large-scale systems",
                "Evolve into Senior Software Engineer"
            ]
        },
        "Software Quality Assurance (QA) / Testing": {
            "Courses": ["Automated Testing with Selenium", "Manual Testing Fundamentals", "API Testing with Postman"],
            "Skills": ["Selenium", "Jenkins", "Performance Testing", "Python/Java"],
            "Certifications": ["ISTQB Foundation Level", "Certified Associate in Software Testing (CAST)"],
            "Internships": ["QA Intern", "Test Automation Intern"],
            "Projects": ["Automated Test Suite for a Web Application", "Bug Tracking Simulation"],
            "Roadmap": [
                "Learn manual testing and bug reporting basics",
                "Pick up an automation tool like Selenium or Cypress",
                "Understand CI/CD pipelines",
                "Start as a QA Engineer"
            ]
        },
        "Systems Security Administrator": {
            "Courses": ["System Administration", "Cyber Security Management", "Linux/Unix Systems"],
            "Skills": ["Linux Administration", "Identity Management", "Audit Logging", "Security Policy Implementation"],
            "Certifications": ["CISSP (Certified Information Systems Security Professional)", "CompTIA Server+"],
            "Internships": ["System Admin Intern", "Security Analyst Intern"],
            "Projects": ["Custom Linux Server with SSH hardening", "User Access Control System"],
            "Roadmap": [
                "Master Linux/Windows server environments",
                "Understand organizational security compliance",
                "Gain deep knowledge in auditing and risk management",
                "Work as a Security Admin"
            ]
        },
        "Technical Support": {
            "Courses": ["IT Service Management (ITIL)", "CompTIA A+", "Technical Writing"],
            "Skills": ["Troubleshooting", "Active Listening", "Remote Support Tools", "Knowledge Base Management"],
            "Certifications": ["CompTIA A+", "Google IT Support Professional Certificate"],
            "Internships": ["IT Support Intern", "Customer Success Intern"],
            "Projects": ["Self-service Helpdesk Portal", "Technical Guide for Common Software Issues"],
            "Roadmap": [
                "Learn basics of hardware and operating systems",
                "Develop strong communication and problem-solving skills",
                "Get certified with CompTIA A+ or Google Support",
                "Apply for IT Support Specialist roles"
            ]
        },
        "UX Designer": {
            "Courses": ["Interaction Design Fundamentals", "User Research Methods", "Visual Design with Figma"],
            "Skills": ["Figma", "Adobe XD", "Wireframing", "Prototyping"],
            "Certifications": ["Google UX Design Professional Certificate", "HCI foundations by IDF"],
            "Internships": ["UX Design Intern", "Product Design Intern"],
            "Projects": ["Mobile App Redesign", "Case Study for a New Web Product"],
            "Roadmap": [
                "Build a strong portfolio on Behance/Dribbble",
                "Learn industry-standard tools like Figma/Sketch",
                "Study User Psychology and Human-Computer Interaction",
                "Apply to Design Agencies or Tech Firms"
            ]
        },
        "Web Developer": {
            "Courses": ["Responsive Web Design", "Modern JavaScript (ES6+)", "React/Vue/Angular Frameworks"],
            "Skills": ["HTML/CSS/JS", "RESTful APIs", "Git", "SEO Basics"],
            "Certifications": ["FreeCodeCamp Full Stack Certification", "Meta Front-End Developer Certificate"],
            "Internships": ["Front-end Developer Intern", "Web Development Intern"],
            "Projects": ["Personal Portfolio Website", "Interactive Web-based Game"],
            "Roadmap": [
                "Master HTML, CSS, and basic JavaScript",
                "Pick a front-end framework (React)",
                "Understand back-end connectivity and databases",
                "Find work as a Front-end or Full-stack Web Dev"
            ]
        }
    }
    
    return recommendations.get(career, {
        "Courses": ["General Computer Science Course"],
        "Skills": ["Problem Solving", "Basic Coding"],
        "Certifications": ["General IT Certification"],
        "Internships": ["IT Generalist Intern"],
        "Projects": ["Cap-stone Project"],
        "Roadmap": ["Continue learning core CS concepts"]
    })