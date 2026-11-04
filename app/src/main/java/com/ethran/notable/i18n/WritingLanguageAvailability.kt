package com.ethran.notable.i18n

import java.io.File

/**
 * Which handwriting languages the tablet's recognizer can actually use. The Onyx service reads each language's
 * resources from a folder named after the code (`tr_TR/`): English and Chinese come with the system, others are
 * downloaded in Boox Notes into `/sdcard/.noteResource/<version>/recognition-assets/resources/`. A language
 * without its folder is not recognized.
 */
object WritingLanguageAvailability {
    private val systemResources = File("/system/recognition_assets/resources")
    private val downloadedRoot = File("/sdcard/.noteResource")

    /** Codes that have resources on this tablet; null when the folders cannot be read (then assume all work). */
    fun installed(system: File = systemResources, downloaded: File = downloadedRoot): Set<String>? {
        val found = mutableSetOf<String>()
        var readable = false
        fun add(dir: File) {
            val names = dir.list() ?: return
            readable = true
            found += names
        }
        add(system)
        downloaded.listFiles()?.forEach { add(File(it, "recognition-assets/resources")) }
        return if (readable) found else null
    }

    fun isAvailable(code: String, installed: Set<String>? = installed()): Boolean = installed == null || code in installed

    /** The language the recognizer really gets: the chosen one when installed, otherwise English. */
    fun effective(code: String, installed: Set<String>? = installed()): String =
        if (isAvailable(code, installed)) code else WritingLanguage.DEFAULT_CODE
}
