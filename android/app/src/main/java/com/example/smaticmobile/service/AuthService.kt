package com.example.smaticmobile.service

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.example.smaticmobile.model.auth.Login
import com.example.smaticmobile.repository.AuthRepository
import com.example.smaticmobile.util.http.Http
import com.example.smaticmobile.util.http.ResponseStatus
import com.google.gson.JsonObject
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext

class AuthService(application: Application): AndroidViewModel(application) {
    private val repository: AuthRepository = Http()
        .init()
        .build()
        .create(AuthRepository::class.java)

    private val _loginFlow = MutableSharedFlow<ResponseStatus<Login>>(replay = 5)

    val loginFlow = _loginFlow.asSharedFlow()

    suspend fun login(email: String, password: String) = viewModelScope.launch(Dispatchers.IO) {
        _loginFlow.emit(ResponseStatus.Loading())

        val requestBody = JsonObject()
        requestBody.addProperty("email", email)
        requestBody.addProperty("password", password)

        val response = withContext(Dispatchers.IO) {
            repository.login(requestBody)
        }

        if (!response.isSuccessful) {
            _loginFlow.emit(
                ResponseStatus.Error(
                    message = "Log In Failed",
                    code = response.code()
                )
            )

            return@launch
        }

        val tokenService = TokenService(getApplication())
        val accessToken = response.body()?.payload?.access_token

        if (accessToken != null) tokenService.store(accessToken)

        _loginFlow.emit(
            ResponseStatus.Success(
                code = response.code(),
                message = "Log In Success",
                payload = response.body()?.payload!!
            )
        )
    }
}