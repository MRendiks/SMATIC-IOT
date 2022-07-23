package com.example.smaticmobile.util.http

sealed class ResponseStatus<out T> {
    class Loading: ResponseStatus<Nothing>()

    data class Success<out R> (
        val code: Int,
        val message: String,
        val payload: R
    ): ResponseStatus<R>()

    data class Error(
        val message: String,
        val code: Int
    ): ResponseStatus<Nothing>()
}