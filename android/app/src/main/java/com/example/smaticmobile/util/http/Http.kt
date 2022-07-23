package com.example.smaticmobile.util.http

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class Http {
    fun init(): Retrofit.Builder {
        return Retrofit
            .Builder()
            .baseUrl("https://smatic-staging.herokuapp.com")
            .addConverterFactory(GsonConverterFactory.create())
    }
}