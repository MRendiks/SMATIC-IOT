package com.example.smaticmobile

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Toast
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import com.example.smaticmobile.service.AuthService
import com.example.smaticmobile.util.http.ResponseStatus
import com.example.smaticmobile.view.ButtonView
import com.google.android.material.textfield.TextInputEditText
import com.google.android.material.textview.MaterialTextView
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        val loginBtn = findViewById<ButtonView>(R.id.login_btn)
        val emailEditText = findViewById<TextInputEditText>(R.id.email_edit_text)
        val passwordEditText = findViewById<TextInputEditText>(R.id.password_edit_text)
        val signInText = findViewById<MaterialTextView>(R.id.sign_in_text)

        val authService = ViewModelProvider(this).get(AuthService::class.java)

        loginBtn.setOnClickListener {
            val email = emailEditText.text.toString()
            val password = passwordEditText.text.toString()

            lifecycleScope.launch(Dispatchers.IO) {
                authService.login(email, password)
            }
        }

        signInText.setOnClickListener {
            val registerIntent = Intent(this, RegisterActivity::class.java)
            startActivity(registerIntent)
        }

        lifecycleScope.launch(Dispatchers.Main) {
            authService.loginFlow.collect {
                when(it) {
                    is ResponseStatus.Loading -> {
                        loginBtn.isEnabled = false
                        loginBtn.text = "Please Wait..."
                    }
                    is ResponseStatus.Success -> {
                        val dashboardIntent = Intent(
                            this@LoginActivity,
                            DashboardActivity::class.java
                        )
                        startActivity(dashboardIntent)
                        finish()
                    }
                    is ResponseStatus.Error -> {
                        loginBtn.isEnabled = true
                        loginBtn.text = "Log In"

                        Toast
                            .makeText(this@LoginActivity, it.message, Toast.LENGTH_SHORT)
                            .show()
                    }
                }
            }
        }
    }
}