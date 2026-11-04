package com.ethran.notable.ui.components

import androidx.compose.material.MaterialTheme
import androidx.compose.material.Text
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.ethran.notable.R
import com.ethran.notable.i18n.AppLanguage
import com.ethran.notable.i18n.LanguagePrefs
import com.ethran.notable.i18n.WritingLanguage
import com.ethran.notable.i18n.WritingLanguageAvailability
import com.ethran.notable.io.OnyxHWREngine

/**
 * The two language choices. App language is the language of menus, labels and dates; writing language is the
 * language of the handwriting recognizer. They are independent: e.g. English app, Turkish handwriting.
 */
@Composable
fun LanguageSettings(onAppLanguageChange: (AppLanguage) -> Unit) {
    val context = LocalContext.current
    var app by remember { mutableStateOf(LanguagePrefs.app(context)) }
    var writing by remember { mutableStateOf(LanguagePrefs.writing(context)) }

    SelectorRow(
        label = stringResource(R.string.app_language),
        options = AppLanguage.entries.map { it to it.nativeName },
        value = app,
        onValueChange = { chosen ->
            if (chosen != app) {
                app = chosen
                onAppLanguageChange(chosen)
            }
        }
    )
    val installed = remember { WritingLanguageAvailability.installed() }
    val notInstalled = stringResource(R.string.writing_language_not_installed)
    val ordered = remember(installed) {
        // Languages the tablet can recognize first, the rest after them.
        WritingLanguage.all.sortedBy { if (WritingLanguageAvailability.isAvailable(it.code, installed)) 0 else 1 }
    }
    SelectorRow(
        label = stringResource(R.string.writing_language),
        options = ordered.map {
            it to if (WritingLanguageAvailability.isAvailable(it.code, installed)) it.nativeName else "${it.nativeName} ($notInstalled)"
        },
        value = writing,
        onValueChange = { chosen ->
            writing = chosen
            LanguagePrefs.setWriting(context, chosen)
            OnyxHWREngine.setLanguage(chosen.code)
        }
    )
    val missing = !WritingLanguageAvailability.isAvailable(writing.code, installed)
    Text(
        text = if (missing) stringResource(R.string.writing_language_missing_hint, writing.nativeName)
        else stringResource(R.string.writing_language_hint),
        style = MaterialTheme.typography.body2,
        fontSize = 13.sp,
        color = MaterialTheme.colors.onSurface.copy(alpha = 0.7f),
        modifier = Modifier.padding(start = 4.dp, bottom = 8.dp)
    )
}
