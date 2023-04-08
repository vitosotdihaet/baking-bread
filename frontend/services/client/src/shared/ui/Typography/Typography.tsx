import {
    FC,
    HTMLAttributes,
    memo,
    ReactNode,
} from 'react';
import {
    Additional,
    classNames,
    Mods,
} from 'shared/lib/classNames/classNames';
import cls from './Typography.module.scss';

type TypographyVariant = 'title' | 'subtitle' | 'p' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'div';
type TypographyAlign = 'center' | 'right' | 'left' | 'inherit';
type TypographyFamily = 'gt' | 'sans'

interface TypographyProps extends HTMLAttributes<HTMLElement> {
    className?: string;
    children: ReactNode;
    variant?: TypographyVariant;
    align?: TypographyAlign;
    family?: TypographyFamily;
    noWrap?: boolean;
    bold?: boolean;
    semibold?: boolean;
}

export const Typography: FC<TypographyProps> = memo((props: TypographyProps) => {
    const {
        className,
        children,
        variant = 'p',
        align = 'left',
        family = 'gt',
        noWrap,
        bold,
        ...otherProps
    } = props;

    const mods: Mods = {
        [cls.noWrap]: noWrap,
        [cls.bold]: bold,
    };

    const additional: Additional = [
        className,
        cls[variant],
        cls[align],
        cls[family],
    ];

    return (
        <>
            {variant === 'p'
                && (
                    <p
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </p>
                )}
            {variant === 'div'
                && (
                    <div
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </div>
                )}
            {variant === 'h1'
                && (
                    <h1
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </h1>
                )}
            {variant === 'h2'
                && (
                    <h2
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </h2>
                )}
            {variant === 'h3'
                && (
                    <h3
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </h3>
                )}
            {variant === 'h4'
                && (
                    <h4
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </h4>
                )}
            {variant === 'h5'
                && (
                    <h5
                        className={classNames(cls.Typography, mods, additional)}
                        {...otherProps}
                    >
                        {children}
                    </h5>
                )}
            {variant === 'title'
                 && (
                     <p
                         className={classNames(cls.Typography, mods, additional)}
                         {...otherProps}
                     >
                         {children}
                     </p>
                 )}
            {variant === 'subtitle'
             && (
                 <p
                     className={classNames(cls.Typography, mods, additional)}
                     {...otherProps}
                 >
                     {children}
                 </p>
             )}
        </>
    );
});
