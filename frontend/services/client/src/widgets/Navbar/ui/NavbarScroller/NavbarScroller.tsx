import { Tab } from '@headlessui/react';
import { useTranslation } from 'next-i18next';
import { FC, memo, useState } from 'react';
import { goodTypesItems } from 'widgets/Navbar/model/goodTypeItems';
import { GoodType } from 'entities/Good';
import { classNames } from 'shared/lib/classNames/classNames';
import { Button } from 'shared/ui/Button/Button';
import { Row } from 'shared/ui/Stack';
import cls from './NavbarScroller.module.scss';

export const NavbarScroller: FC = memo(() => {
    const { t } = useTranslation();
    const [selected, setSelected] = useState('Breads');

    const onClickGoodType = (goodType: GoodType) => () => {
        setSelected(goodType.name);
    };

    return (
        <Tab.Group>
            <Tab.List>
                <Row
                    align='center'
                    gap='8'
                    className={cls.scroller}
                >
                    {goodTypesItems.map((goodType) => {
                        const isSelected = goodType.name === selected;

                        return (
                            <Tab
                                as='span'
                                key={goodType.id}
                                className={cls.tab}
                            >
                                <Button
                                    className={classNames('', { [cls.selected]: isSelected })}
                                    onClick={onClickGoodType(goodType)}
                                    variant={isSelected ? 'accent' : 'secondary'}
                                    size='small'
                                    fullWidth={false}
                                >
                                    {t(goodType.name)}
                                </Button>
                            </Tab>
                        );
                    })}
                </Row>
            </Tab.List>
        </Tab.Group>
    );
});
