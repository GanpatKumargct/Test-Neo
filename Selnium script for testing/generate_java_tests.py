import os
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
    
    java_code = f"""import org.openqa.selenium.By;
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
    file_path = os.path.join(output_dir, f"test_scenario_{scenario_id}.java")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(java_code)

if __name__ == "__main__":
    output_dir = r"e:\Test Neo\Selnium script for testing\Script with Java"
    os.makedirs(output_dir, exist_ok=True)
    for i in range(1, 61):
        generate_java_test(i, output_dir)
