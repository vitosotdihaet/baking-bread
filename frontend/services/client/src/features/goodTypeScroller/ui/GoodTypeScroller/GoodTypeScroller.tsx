import { Tab } from '@headlessui/react';
import { useTranslation } from 'next-i18next';
import {
    FC,
    memo,
    useCallback,
    useEffect,
} from 'react';
import { useSelector } from 'react-redux';
import { GoodType } from 'entities/Good';
import { classNames } from 'shared/lib/classNames/classNames';
import { DynamicModuleLoader, ReducersList } from 'shared/lib/components/DynamicModuleLoader/DynamicModuleLoader';
import { useAppDispatch } from 'shared/lib/hooks/useAppDispatch/useAppDispatch';
import { Button } from 'shared/ui/Button/Button';
import { Row } from 'shared/ui/Stack';
import { getSelectedType } from '../../model/selectors/getSelectedType';
import { goodTypeScrollerActions, goodTypeScrollerReducer } from '../../model/slice/goodTypeScrollerSlice';
import cls from './GoodTypeScroller.module.scss';

interface GoodTypeScrollerProps {
    className?: string;
    goodTypes: GoodType[];
}

const reducers: ReducersList = {
    goodTypeScroller: goodTypeScrollerReducer,
};

export const GoodTypeScroller: FC<GoodTypeScrollerProps> = memo((props: GoodTypeScrollerProps) => {
    const {
        className,
        goodTypes,
    } = props;
    const { t } = useTranslation();
    const selectedType = useSelector(getSelectedType);
    const dispatch = useAppDispatch();

    const onClickGoodType = useCallback((goodType: GoodType) => () => {
        dispatch(goodTypeScrollerActions.setSelectedType(goodType.name));
    }, [dispatch]);

    useEffect(() => {
        if (goodTypes) {
            dispatch(goodTypeScrollerActions.initSelectedType(goodTypes[0].name));
        }
    }, [dispatch, goodTypes]);

    if (!goodTypes) {
        return null;
    }

    const renderGoodType = (goodType: GoodType, isSelected: boolean) => {
        if (goodType.goodsCount < 1) {
            return null;
        }

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
                    size='medium'
                    padding='smPadding'
                    fullWidth={false}
                    key={goodType.id}
                    href={`#${goodType.name}`}
                    as='a'
                >
                    {t(goodType.name)}
                </Button>
            </Tab>
        );
    };

    return (
        <DynamicModuleLoader reducers={reducers}>
            <Tab.Group>
                <Tab.List className={classNames('', {}, [className])}>
                    <Row
                        align='center'
                        gap='8'
                        className={classNames(cls.scroller)}
                    >
                        {goodTypes.map((goodType) => renderGoodType(goodType, goodType.name === selectedType))}
                    </Row>
                </Tab.List>
            </Tab.Group>
        </DynamicModuleLoader>
    );
});
