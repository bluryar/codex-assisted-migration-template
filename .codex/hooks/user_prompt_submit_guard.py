#!/usr/bin/env python3
import json
import sys


IMPLEMENTATION_KEYWORDS = (
    "implement",
    "fix",
    "refactor",
    "migrate",
    "optimize",
    "rewrite",
    "run through",
    "make it pass",
    "实现",
    "修复",
    "重构",
    "迁移",
    "优化",
    "改写",
    "跑通",
    "对齐",
)

STRICT_KEYWORDS = (
    "api",
    "public",
    "default path",
    "fallback",
    "benchmark",
    "optimize",
    "runtime",
    "ownership",
    "lifetime",
    "state",
    "output",
    "cache",
    "bridge",
    "host",
    "device",
    "接口",
    "公共",
    "默认",
    "回退",
    "桥接",
    "性能",
    "优化",
    "运行时",
    "所有权",
    "生命周期",
    "状态",
    "输出",
    "缓存",
    "热路径",
)


def main() -> None:
    data = json.load(sys.stdin)
    prompt = (data.get("prompt") or "").lower()

    is_implementation = any(word in prompt for word in IMPLEMENTATION_KEYWORDS)
    needs_strict_preflight = any(word in prompt for word in STRICT_KEYWORDS)

    if is_implementation and needs_strict_preflight:
        payload = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": (
                    "High-risk migration prompt detected. Write the five-line working brief, "
                    "then use strict preflight before coding: stage, migration position, timing, "
                    "permanent boundary, freeze/hide/delete target, unavoidable additions, "
                    "host/bridge/dual-path/ownership impact, API ownership, temporary-path delete "
                    "condition, convergence metric, smallest reversible slice, and stop condition."
                )
            }
        }
    elif is_implementation:
        payload = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": (
                    "Implementation-style prompt detected. Write the five-line working brief, "
                    "then confirm stage, permanent boundary, out-of-scope items, evidence required, "
                    "and stop conditions before coding."
                )
            }
        }
    else:
        payload = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": (
                    "Keep hot context short. Use historical docs only on demand."
                )
            }
        }

    print(json.dumps(payload))


if __name__ == "__main__":
    main()
