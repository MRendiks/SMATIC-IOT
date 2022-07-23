package com.example.smaticmobile.util.http

data class ApiResponseBody<T> (
    val code: Number,
    val message: String,
    val payload: T
)