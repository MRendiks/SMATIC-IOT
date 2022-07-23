package com.example.smaticmobile.view

import android.content.Context
import android.util.AttributeSet
import android.util.Log
import android.view.LayoutInflater
import android.widget.LinearLayout
import androidx.core.content.ContextCompat
import com.example.smaticmobile.R

class StepTrackView(context: Context, attrs: AttributeSet): LinearLayout(context, attrs)  {
    var trackView: LinearLayout

    var active = false
        set(value) {
            trackView.background = ContextCompat.getDrawable(
                context,
                if (value) R.drawable.bg_gradient_primary else R.drawable.bg_track_inactive
            )

            field = value
        }

    init {
        LayoutInflater.from(context).inflate(R.layout.view_step_track, this)
        trackView = findViewById(R.id.track)

        val styledAttrs = context.obtainStyledAttributes(attrs, R.styleable.StepTrackView)
        active = styledAttrs.getBoolean(R.styleable.StepTrackView_active, false)
    }
}