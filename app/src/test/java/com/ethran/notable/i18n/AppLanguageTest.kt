package com.ethran.notable.i18n

import kotlin.test.assertEquals
import kotlin.test.assertTrue
import org.junit.Test

class AppLanguageTest {
    @Test fun `english is the default for both languages`() {
        assertEquals(AppLanguage.English, AppLanguage.Default)
        assertEquals(AppLanguage.English, AppLanguage.fromTag(null))
        assertEquals(AppLanguage.English, AppLanguage.fromTag("xx"))
        assertEquals("en_US", WritingLanguage.DEFAULT_CODE)
        assertEquals("en_US", WritingLanguage.fromCode(null).code)
        assertEquals("en_US", WritingLanguage.fromCode("nope").code)
    }

    @Test fun `app languages are English Turkish Polish Spanish and Chinese`() {
        assertEquals(listOf("en", "tr", "pl", "es", "zh"), AppLanguage.entries.map { it.tag })
        assertEquals(AppLanguage.Turkish, AppLanguage.fromTag("tr"))
        assertEquals("zh", AppLanguage.Chinese.locale.language)
        assertEquals("CN", AppLanguage.Chinese.locale.country)
    }

    @Test fun `writing languages have unique codes and include Turkish`() {
        val codes = WritingLanguage.all.map { it.code }
        assertEquals(codes.size, codes.toSet().size)
        assertEquals("Türkçe", WritingLanguage.fromCode("tr_TR").nativeName)
        assertTrue(codes.containsAll(listOf("en_US", "tr_TR", "es_ES", "zh_CN", "pl_PL")))
    }
}
