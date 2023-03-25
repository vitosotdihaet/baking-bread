export type Mods = Record<string, string | boolean | undefined>
export type Additional = Array<string | undefined>

export function classNames(cls: string, mods: Mods = {}, additional: Additional = []): string {
    return [
        cls,
        ...additional.filter(Boolean),
        ...Object.entries(mods)
            .filter(([className, value]) => Boolean(value))
            .map(([className]) => className),
    ].join(' ');
}
