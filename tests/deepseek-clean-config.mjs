// Narrow source-configuration regression. Does not assert runtime egress safety.
import {readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
const root=new URL('../',import.meta.url);
const text=await readFile(new URL('packages/bundle/base/cordis.patch.yml',root),'utf8');
for(const id of ['deepseek-llm-api-extensions','session-log-deepseek','plugin-package-inventory-deepseek','deepseek-account','web-search-deepseek','llm-deepseek','llm-deepseek-account']) {
 const escaped=id.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
 assert.match(text,new RegExp('id: '+escaped+'\\s*\\n(?:(?!\\n\\s*- id:)[\\s\\S])*?disabled: true'));
}
assert.match(text,/baseURL:\s*http:\/\/127\.0\.0\.1:8000\/v1/);
assert.match(text,/provider:\s*local-offline/);
console.log('PASS: source configuration assertions only; runtime NOT VERIFIED');
