import { useTranslation } from 'next-i18next';
import { FC } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import { AppLink } from 'shared/ui/AppLink/AppLink';
import { Icon } from 'shared/ui/Icon/Icon';
import { Column, Row } from 'shared/ui/Stack';
import { Typography } from 'shared/ui/Typography/Typography';
import { toolbarItems } from '../../consts/toolbarItems';
import cls from './Toolbar.module.scss';

interface ToolbarProps {
    className?: string;
}

export const Toolbar: FC<ToolbarProps> = (props) => {
    const { className } = props;
    const { t } = useTranslation();

    return (
        <Row justify='around' className={classNames(cls.Toolbar, {}, [className])}>
            {toolbarItems.map((item) => (
                <AppLink
                    key={item.path}
                    href={item.path}
                    className={cls.tool}
                >
                    <Column
                        align='center'
                        gap='4'
                    >
                        <Icon SVG={item.Icon} />
                        <Typography
                            size='xs'
                            variant='span'
                        >
                            {t(item.label)}
                        </Typography>
                    </Column>
                </AppLink>
            ))}
        </Row>
    );
};
