#!/system/bin/sh
MODDIR=${0%/*}
pm grant com.miui.mishare.connectivity android.permission.SYSTEM_ALERT_WINDOW
pm grant com.miui.mishare.connectivity android.permission.INTERNET
pm grant com.miui.mishare.connectivity android.permission.ACCESS_COARSE_LOCATION
pm grant com.miui.mishare.connectivity android.permission.ACCESS_FINE_LOCATION
pm grant com.miui.mishare.connectivity android.permission.READ_EXTERNAL_STORAGE
pm grant com.miui.mishare.connectivity android.permission.WRITE_EXTERNAL_STORAGE
pm grant com.miui.mishare.connectivity android.permission.WRITE_SECURE_SETTINGS
