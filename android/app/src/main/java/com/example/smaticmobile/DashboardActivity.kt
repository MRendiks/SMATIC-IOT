package com.example.smaticmobile

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.LinearLayout
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class DashboardActivity : AppCompatActivity() {
    val scope = CoroutineScope(Dispatchers.IO)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_dashboard)
        val contentView = findViewById<LinearLayout>(R.id.content)
        val loadingView = findViewById<LinearLayout>(R.id.loading)

        loadingView.visibility = View.VISIBLE
        contentView.visibility = View.GONE

        scope.launch {
            delay(2000L)
            withContext(Dispatchers.Main) {
                loadingView.visibility = View.GONE
                contentView.visibility = View.VISIBLE
            }
        }
    }
}