import os
import shutil
import random

def get_random_statement():
    locators = [
        ('By.id', '"user_name"'),
        ('By.className', '"nav-item"'),
        ('By.xpath', '"//button[@type=\'submit\']"'),
        ('By.cssSelector', '".promo-code"'),
        ('By.linkText', '"Log Out"'),
        ('By.id', '"checkout_btn"'),
        ('By.name', '"password_field"')
    ]
    actions = ['click()', 'sendKeys("test_data_{}")', 'isDisplayed()']
    
    loc, val = random.choice(locators)
    action = random.choice(actions)
    
    if action.startswith('send'):
        action = action.format(random.randint(100, 999))
    
    if action == 'isDisplayed()':
        return f'            if (!driver.findElement({loc}({val})).isDisplayed()) {{\n                System.out.println("Element not displayed");\n            }}'
    
    return f'            driver.findElement({loc}({val})).{action};'

def generate_java_test(scenario_id, output_dir):
    class_name = f"TestScenario{scenario_id}"
    
    body = []
    num_steps = random.randint(8, 15)
    for _ in range(num_steps):
        r = random.random()
        if r < 0.1:
            body.append(f'            Thread.sleep(2000);')
        elif r < 0.2:
            body.append(f'            if (!driver.getTitle().contains("Dashboard")) {{\n                System.out.println("Dashboard not in title");\n            }}')
        else:
            body.append(get_random_statement())
            
    body_str = "\n".join(body)
    
    java_code = f"""package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class {class_name} {{
    public static void executeTest{scenario_id}() {{
        /*
         * Dummy test run for scenario {scenario_id}
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_{scenario_id}");

        try {{
{body_str}
        }} catch (Exception e) {{
            e.printStackTrace();
        }} finally {{
            driver.quit();
        }}
    }}
    
    public static void main(String[] args) {{
        executeTest{scenario_id}();
    }}
}}
"""
    file_path = os.path.join(output_dir, f"{class_name}.java")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(java_code)

def create_pom(java_dir):
    pom_content = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example.test</groupId>
    <artifactId>selenium-tests</artifactId>
    <version>1.0-SNAPSHOT</version>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Selenium WebDriver -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>4.19.1</version>
        </dependency>
    </dependencies>
</project>
"""
    with open(os.path.join(java_dir, "pom.xml"), "w", encoding="utf-8") as f:
        f.write(pom_content)

if __name__ == "__main__":
    base_dir = r"e:\Test Neo\Selnium script for testing\Script with Java"
    
    # Clean up old files in the base directory
    try:
        for item in os.listdir(base_dir):
            item_path = os.path.join(base_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
    except FileNotFoundError:
        pass
            
    # Create maven structure
    src_test_java_dir = os.path.join(base_dir, "src", "test", "java", "testscenario")
    os.makedirs(src_test_java_dir, exist_ok=True)
    
    create_pom(base_dir)
    
    for i in range(1, 61):
        generate_java_test(i, src_test_java_dir)
