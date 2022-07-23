package com.example.smaticmobile.view

import android.content.Context
import android.graphics.Paint
import android.util.AttributeSet
import android.view.LayoutInflater
import android.widget.TextView
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.core.content.ContextCompat
import com.example.smaticmobile.R

class InvoiceItemView(context: Context, attrs: AttributeSet): ConstraintLayout(context, attrs) {
    lateinit var dateTextView: TextView
    lateinit var elapsedTextView: TextView
    lateinit var billTextView: TextView
    lateinit var statusTextView: TextView

    var paid = false
        set(value) {
            statusTextView.text = if (value) "Paid" else "Unpaid"
            billTextView.paintFlags = if (value) Paint.STRIKE_THRU_TEXT_FLAG else Paint.ANTI_ALIAS_FLAG

            val color = ContextCompat.getColor(
                context,
                if (value) R.color.gray_500 else R.color.red_500
            )

            statusTextView.setTextColor(color)
            billTextView.setTextColor(color)

            field = value
        }

    var date = ""
        set(value) {
            dateTextView.text = value
            field = value
        }

    var bill = 0
        set(value) {
            val text = "Rp${value}"

            billTextView.text = text

            field = value
        }

    var elapsed = ""
        set(value) {
            elapsedTextView.text = value

            field = value
        }

    init {
        LayoutInflater
            .from(context)
            .inflate(R.layout.view_invoice_item, this)

        dateTextView = findViewById(R.id.date)
        elapsedTextView = findViewById(R.id.elapsed)
        billTextView = findViewById(R.id.bill)
        statusTextView = findViewById(R.id.status)

        val styledAttrs = context.obtainStyledAttributes(attrs, R.styleable.InvoiceItemView)
        paid = styledAttrs.getBoolean(R.styleable.InvoiceItemView_paid, false)
        elapsed = styledAttrs.getString(R.styleable.InvoiceItemView_elapsed) ?: ""
        date = styledAttrs.getString(R.styleable.InvoiceItemView_date) ?: ""

        val billAttr = styledAttrs.getString(R.styleable.InvoiceItemView_bill)
        bill = billAttr?.toInt() ?: 0
    }
}