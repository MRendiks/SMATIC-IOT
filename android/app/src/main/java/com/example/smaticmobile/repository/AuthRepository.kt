package com.example.smaticmobile.repository

import com.example.smaticmobile.model.auth.Login
import com.example.smaticmobile.util.http.ApiResponseBody
import com.google.gson.JsonObject
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

interface AuthRepository {
    @POST("/api/auth/login")
    suspend fun login(@Body body: JsonObject): Response<ApiResponseBody<Login>>
}