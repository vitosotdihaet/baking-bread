import { ComponentMeta, ComponentStory } from '@storybook/react';
import React from 'react';
import { Button } from './Button';

export default {
    title: 'shared/Button',
    component: Button,
    args: {
        fullWidth: false,
        children: 'Savory pastries',
    },
} as ComponentMeta<typeof Button>;

const Template: ComponentStory<typeof Button> = (args) => <Button {...args} />;

export const Primary = Template.bind({});
Primary.args = {
    variant: 'primary',
};

export const Secondary = Template.bind({});
Secondary.args = {
    variant: 'secondary',
};

export const Outlined = Template.bind({});
Outlined.args = {
    variant: 'outlined',
};

export const Accent = Template.bind({});
Accent.args = {
    variant: 'accent',
};

export const Clear = Template.bind({});
Clear.args = {
    variant: 'clear',
};

export const Disabled = Template.bind({});
Disabled.args = {
    disabled: true,
};

export const FullWidth = Template.bind({});
FullWidth.args = {
    fullWidth: true,
};

export const SizeSmall = Template.bind({});
SizeSmall.args = {
    size: 'small',
};

export const SizeMedium = Template.bind({});
SizeMedium.args = {
    size: 'medium',
};

export const SizeLarge = Template.bind({});
SizeLarge.args = {
    size: 'large',
};

export const AlignContentLeft = Template.bind({});
AlignContentLeft.args = {
    alignContent: 'left',
};

export const AlignContentCenter = Template.bind({});
AlignContentCenter.args = {
    alignContent: 'center',
};

export const AlignContentRight = Template.bind({});
AlignContentRight.args = {
    alignContent: 'right',
};

export const BorderRadiusXS = Template.bind({});
BorderRadiusXS.args = {
    radius: 'xs',
};

export const BorderRadiusSM = Template.bind({});
BorderRadiusSM.args = {
    radius: 'sm',
};

export const BorderRadiusMD = Template.bind({});
BorderRadiusMD.args = {
    radius: 'md',
};

export const BorderRadiusLG = Template.bind({});
BorderRadiusLG.args = {
    radius: 'lg',
};

export const BorderRadiusXL = Template.bind({});
BorderRadiusXL.args = {
    radius: 'xl',
};

export const WithBefore = Template.bind({});
WithBefore.args = {
    before: <>Now /</>,
};

export const WithAfter = Template.bind({});
WithAfter.args = {
    after: <>/ 3 pcs</>,
};

export const WithBeforeAndAfter = Template.bind({});
WithBeforeAndAfter.args = {
    before: <>Now /</>,
    after: <>/ 3 pcs</>,
};

export const Uppercase = Template.bind({});
Uppercase.args = {
    uppercase: true,
};

export const AsLink = Template.bind({});
AsLink.args = {
    as: 'a',
    href: '/',
};

export const Loading = Template.bind({});
Loading.args = {
    loading: true,
};
