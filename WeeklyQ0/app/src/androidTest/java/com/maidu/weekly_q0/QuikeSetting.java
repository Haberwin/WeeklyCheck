package com.maidu.weekly_q0;

import android.support.test.InstrumentationRegistry;
import android.support.test.runner.AndroidJUnit4;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

import androidx.test.uiautomator.UiDevice;
import androidx.test.uiautomator.UiObject;
import androidx.test.uiautomator.UiObjectNotFoundException;
import androidx.test.uiautomator.UiSelector;

@RunWith(AndroidJUnit4.class)
public class QuikeSetting {
    private UiDevice device = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation());

    @Test
    public void testCamera() throws UiObjectNotFoundException {
        UiObject camera=device.findObject(new UiSelector().text("图库"));
        camera.click();
    }
    @Test
    public void testAOSP() throws UiObjectNotFoundException {
        UiObject cal=device.findObject(new UiSelector().text("计算器"));
        cal.click();
    }
}
