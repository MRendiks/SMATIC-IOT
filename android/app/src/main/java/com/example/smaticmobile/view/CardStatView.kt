package com.example.smaticmobile.view

import android.content.Context
import android.util.AttributeSet
import android.util.Log
import android.view.LayoutInflater
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import com.example.smaticmobile.R

class CardStatView(context: Context, attrs: AttributeSet): ConstraintLayout(context, attrs) {
    lateinit var headlineTextView: TextView
    lateinit var captionTextView: TextView

    var headline: String = ""
        set(value) {
            headlineTextView.text = value
            field = value
        }
    var caption: String = ""
        set(value) {
            captionTextView.text = value
            field = value
        }

    init {
        LayoutInflater.from(context).inflate(R.layout.view_card_stat, this)

        headlineTextView = findViewById(R.id.headline)
        captionTextView = findViewById(R.id.caption)

        val styledAttrs = context.obtainStyledAttributes(attrs, R.styleable.CardStatView)
        headline = styledAttrs.getString(R.styleable.CardStatView_headline) ?: ""
        caption = styledAttrs.getString(R.styleable.CardStatView_caption) ?: ""
    }
}