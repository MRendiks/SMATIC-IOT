package com.example.smaticmobile.view

import android.content.Context
import android.util.AttributeSet
import android.view.LayoutInflater
import android.widget.LinearLayout
import android.widget.TextView
import androidx.core.content.ContextCompat
import com.example.smaticmobile.R

class StepThumbView(context: Context, attrs: AttributeSet): LinearLayout(context, attrs) {
    var stepText: TextView
    var stepContainer: LinearLayout

    var step = 1
        set(value) {
            stepText.text = value.toString()

            field = value
        }

    var active = false
        set(value) {
            stepContainer.background = ContextCompat.getDrawable(
                context,
                if (value) R.drawable.bg_step_active else R.drawable.bg_step_inactive
            )
            stepText.setTextColor(
                ContextCompat.getColor(
                    context,
                    if (value) R.color.white else R.color.black_500
                )
            )

            field = value
        }

    init {
        LayoutInflater.from(context).inflate(R.layout.view_step_thumb, this)

        stepText = findViewById(R.id.step)
        stepContainer = findViewById(R.id.container)

        val styledAttrs = context.obtainStyledAttributes(attrs, R.styleable.StepThumbView)
        active = styledAttrs.getBoolean(R.styleable.StepThumbView_active, false)
        step = styledAttrs.getInteger(R.styleable.StepThumbView_step, 1)
    }
}