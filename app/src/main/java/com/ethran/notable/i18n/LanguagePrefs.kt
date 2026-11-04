package com.ethran.notable.i18n

import android.content.Context
import android.content.SharedPreferences

/**
 * Where the two language choices live. They are read before the database is open (the activity needs the app
 * language to build its resources), so they sit in SharedPreferences, not in AppSettings. Defaults: English / English.
 */
object LanguagePrefs {
    private const val FILE = "language"
    private const val KEY_APP = "app_language"
    private const val KEY_WRITING = "writing_language"

    private fun prefs(context: Context): SharedPreferences =
        context.applicationContext.getSharedPreferences(FILE, Context.MODE_PRIVATE)

    fun app(context: Context): AppLanguage = AppLanguage.fromTag(prefs(context).getString(KEY_APP, null))

    fun setApp(context: Context, language: AppLanguage) {
        prefs(context).edit().putString(KEY_APP, language.tag).apply()
    }

    fun writing(context: Context): WritingLanguage =
        WritingLanguage.fromCode(prefs(context).getString(KEY_WRITING, null))

    fun setWriting(context: Context, language: WritingLanguage) {
        prefs(context).edit().putString(KEY_WRITING, language.code).apply()
    }
}
