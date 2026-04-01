package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario8 {
    public static void executeTest8() {
        /*
         * Dummy test run for scenario 8
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_8");

        try {
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_327");
            driver.findElement(By.className("nav-item")).click();
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.id("user_name")).sendKeys("test_data_726");
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.className("nav-item")).click();
            if (!driver.findElement(By.className("nav-item")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.linkText("Log Out")).click();
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest8();
    }
}
